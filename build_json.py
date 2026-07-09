#!/usr/bin/env python3
"""
Regenerate data/gradeN.json from data/gradeN.ts, the source of truth for
curriculum content. The sync pipeline (src/lib/curriculum-sync.server.ts in
the gradesbooster-lovable repo) only ever reads the committed .json files
from GitHub -- it never touches .ts. So any edit to a .ts file (new days,
content fixes, or fetch_video_ids.py filling in videoUrl) is invisible to
the live site until this script re-exports it to .json and that .json is
committed and pushed.

Rather than re-implementing a TS object-literal parser, this actually
imports each grade{N}.ts as a real ES module (via `tsx`, the same tool the
app's dev server uses) and JSON.stringifies its default export. That's the
only way to be 100% faithful to the file's real structure -- regex-based
reconstruction is exactly the kind of thing that silently drops a field or
mis-escapes a quote somewhere in a 250KB file and nobody notices until a
lesson breaks in production.

The one wrinkle: grade{N}.ts starts with `import type { DayContent } from
"@/types"`, a path alias that only resolves inside the Next.js app's
tsconfig. That import is type-only (erased at compile time, never touches
runtime), so it's safe to strip before handing the file to tsx standalone.

Usage:
  python3 build_json.py                 # regenerate all 13 grades
  python3 build_json.py --grade 3       # just grade3.json
  python3 build_json.py --check         # exit non-zero if any .json is
                                         # stale relative to its .ts (no writes)

No third-party Python dependencies. Requires `npx` (Node) on PATH -- tsx
itself is fetched automatically by npx the first time this runs.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

RUNNER_TEMPLATE = (
    # Namespace import, then peel off `.default` until we hit the actual
    # array. Run standalone (no app tsconfig in scope), esbuild's CJS/ESM
    # interop wraps `export default X` inconsistently -- observed both
    # `mod.default === X` and `mod.default.default === X` depending on
    # esbuild's mood, with no tsconfig signal available here to control
    # which. Unwrapping in a loop is robust to either.
    'import * as mod from "./{module_name}";\n'
    'let curriculum: unknown = mod;\n'
    'while (curriculum && !Array.isArray(curriculum) && typeof curriculum === "object" && "default" in curriculum) {{\n'
    '  curriculum = (curriculum as any).default;\n'
    '}}\n'
    'if (!Array.isArray(curriculum)) {{\n'
    '  throw new Error("Could not resolve a default-exported array from {module_name}");\n'
    '}}\n'
    'process.stdout.write(JSON.stringify(curriculum));\n'
)


def export_grade_to_json_string(grade):
    """Imports data/gradeN.ts as a real module via tsx and returns its
    default export serialized as a JSON string. Raises RuntimeError with
    the underlying tsx/node stderr on failure."""
    ts_path = os.path.join(DATA_DIR, f'grade{grade}.ts')
    src = open(ts_path, encoding='utf-8').read()
    # Strip the type-only `@/types` import -- erased at compile time
    # anyway, and the path alias doesn't resolve outside the Next.js app.
    stripped = re.sub(r'^import type .*\n', '', src, count=1, flags=re.MULTILINE)

    # Scratch files live in the system temp dir, not inside the repo: some
    # sandboxed/mounted checkouts of this repo refuse to let a process
    # delete files it just created (even ones it owns with 0700 perms), so
    # writing-then-cleaning-up inside DATA_DIR is unreliable. /tmp doesn't
    # have that problem, and since the only import we strip out was
    # type-only, the module has no remaining relative imports to resolve.
    scratch_dir = tempfile.mkdtemp(prefix='gradebooster_build_json_')
    try:
        module_path = os.path.join(scratch_dir, f'grade{grade}.ts')
        with open(module_path, 'w', encoding='utf-8') as f:
            f.write(stripped)

        runner_path = os.path.join(scratch_dir, 'runner.mts')
        with open(runner_path, 'w', encoding='utf-8') as f:
            f.write(RUNNER_TEMPLATE.format(module_name=f'grade{grade}.ts'))

        result = subprocess.run(
            ['npx', '--yes', 'tsx', 'runner.mts'],
            cwd=scratch_dir,
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or 'tsx exited non-zero with no stderr')
        return result.stdout
    finally:
        import shutil
        shutil.rmtree(scratch_dir, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--grade', type=int, default=None, help='only regenerate this grade (0-12)')
    parser.add_argument('--check', action='store_true', help="report staleness, don't write; exits 1 if any grade is stale")
    args = parser.parse_args()

    grades = [args.grade] if args.grade is not None else list(range(13))
    stale_or_failed = []

    for g in grades:
        ts_path = os.path.join(DATA_DIR, f'grade{g}.ts')
        json_path = os.path.join(DATA_DIR, f'grade{g}.json')
        if not os.path.exists(ts_path):
            print(f'grade{g}: SKIP (no grade{g}.ts)', file=sys.stderr)
            continue
        try:
            json_str = export_grade_to_json_string(g)
            new_data = json.loads(json_str)
        except Exception as e:
            print(f'grade{g}: ERROR {e}', file=sys.stderr)
            stale_or_failed.append(g)
            continue

        old_data = None
        if os.path.exists(json_path):
            try:
                old_data = json.load(open(json_path, encoding='utf-8'))
            except Exception:
                old_data = None

        if args.check:
            if old_data != new_data:
                stale_or_failed.append(g)
                print(f'grade{g}: STALE (.json does not match .ts)')
            else:
                print(f'grade{g}: up to date')
            continue

        if old_data == new_data:
            print(f'grade{g}.json: already up to date ({len(new_data)} days)')
            continue

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f'grade{g}.json: written ({len(new_data)} days)')

    if args.check and stale_or_failed:
        print(f'\n{len(stale_or_failed)} grade(s) stale or failed: {stale_or_failed}', file=sys.stderr)
        sys.exit(1)
    if not args.check and stale_or_failed:
        print(f'\n{len(stale_or_failed)} grade(s) failed to build: {stale_or_failed}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
