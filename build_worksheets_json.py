#!/usr/bin/env python3
"""
Regenerate data/gradeN_worksheets.json from data/gradeN_worksheets.ts, the
source of truth for the standalone optional-worksheet content (Project Plan
item 8). Mirrors build_json.py exactly, just targeting the worksheets file
pair instead of the day-based curriculum file pair -- see that script's
docstring for the full rationale (real tsx import > regex reconstruction).

Usage:
  python3 build_worksheets_json.py                 # regenerate all 13 grades
  python3 build_worksheets_json.py --grade 3        # just grade3_worksheets.json
  python3 build_worksheets_json.py --check          # report staleness, no writes

No third-party Python dependencies. Requires `npx` (Node) on PATH.
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
    'import * as mod from "./{module_name}";\n'
    'let worksheets: unknown = mod;\n'
    'while (worksheets && !Array.isArray(worksheets) && typeof worksheets === "object" && "default" in worksheets) {{\n'
    '  worksheets = (worksheets as any).default;\n'
    '}}\n'
    'if (!Array.isArray(worksheets)) {{\n'
    '  throw new Error("Could not resolve a default-exported array from {module_name}");\n'
    '}}\n'
    'process.stdout.write(JSON.stringify(worksheets));\n'
)


def export_grade_to_json_string(grade):
    ts_path = os.path.join(DATA_DIR, f'grade{grade}_worksheets.ts')
    src = open(ts_path, encoding='utf-8').read()
    # Strip any type-only import (none expected in this pipeline, but
    # harmless/no-op if absent -- kept for parity with build_json.py in
    # case a future pass adds a real WorksheetContent type).
    stripped = re.sub(r'^import type .*\n', '', src, count=1, flags=re.MULTILINE)

    scratch_dir = tempfile.mkdtemp(prefix='gradebooster_build_worksheets_json_')
    try:
        module_path = os.path.join(scratch_dir, f'grade{grade}_worksheets.ts')
        with open(module_path, 'w', encoding='utf-8') as f:
            f.write(stripped)

        runner_path = os.path.join(scratch_dir, 'runner.mts')
        with open(runner_path, 'w', encoding='utf-8') as f:
            f.write(RUNNER_TEMPLATE.format(module_name=f'grade{grade}_worksheets.ts'))

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
        ts_path = os.path.join(DATA_DIR, f'grade{g}_worksheets.ts')
        json_path = os.path.join(DATA_DIR, f'grade{g}_worksheets.json')
        if not os.path.exists(ts_path):
            print(f'grade{g}: SKIP (no grade{g}_worksheets.ts)', file=sys.stderr)
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
            print(f'grade{g}_worksheets.json: already up to date ({len(new_data)} worksheets)')
            continue

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f'grade{g}_worksheets.json: written ({len(new_data)} worksheets)')

    if args.check and stale_or_failed:
        print(f'\n{len(stale_or_failed)} grade(s) stale or failed: {stale_or_failed}', file=sys.stderr)
        sys.exit(1)
    if not args.check and stale_or_failed:
        print(f'\n{len(stale_or_failed)} grade(s) failed to build: {stale_or_failed}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
