#!/usr/bin/env python3
"""
Trim the "correct answer is always the longest/most detailed option" tell.

An audit found that in many grade files, the correct answer is disproportionately
longer than the three wrong options -- often because it has a short core claim
followed by " -- extra justification" tacked on (e.g. grade11 correct answers
averaged 141 characters vs 27 for wrong answers, and were the uniquely longest
option 96% of the time). A test-savvy kid could just pick the longest, most
detailed-sounding option without reading anything.

This script ONLY touches the correct answer's text, ONLY when it is
disproportionately longer than the wrong options AND contains an em dash
(" -- " or "--") with a substantial claim before it. It truncates at the dash,
keeping the short core claim and dropping the trailing justification clause.
Wrong options and question text are never touched. Cases without a clean
em-dash split are left alone (flagged in the report) since safely shortening
those needs human judgement, not a mechanical rule.

Usage:
  python3 fix_answer_length_bias.py --dry-run     # report only
  python3 fix_answer_length_bias.py                # apply
  python3 fix_answer_length_bias.py --grade 11     # just one grade
"""
import re
import json
import argparse
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

STR = r'"(?:[^"\\]|\\.)*"'
OPTIONS = r'\[\s*' + STR + r'(?:\s*,\s*' + STR + r')*\s*\]'
Q_OBJ = re.compile(r'\{q:(' + STR + r'), options:(' + OPTIONS + r'), answer:(\d+)\}')

LENGTH_RATIO_THRESHOLD = 1.8
MIN_LENGTH_TO_CONSIDER = 40
MIN_CORE_CLAIM_LEN = 15


def find_dash_split(text):
    """Return (core, tail) split at the first em dash/double-hyphen, or None."""
    for sep in (' — ', '—', ' -- '):
        idx = text.find(sep)
        if idx >= MIN_CORE_CLAIM_LEN:
            return text[:idx].rstrip(), text[idx + len(sep):]
    return None


def process_file(path, dry_run):
    text = open(path, encoding='utf-8').read()
    changed = False
    stats = {'trimmed': 0, 'left_long_no_dash': 0}

    def repl(m):
        nonlocal changed
        q_raw, options_raw, answer_raw = m.group(1), m.group(2), int(m.group(3))
        options = json.loads(options_raw)
        if len(options) != 4:
            return m.group(0)

        lens = [len(o) for o in options]
        wrong_avg = sum(l for i, l in enumerate(lens) if i != answer_raw) / 3
        correct = options[answer_raw]

        if lens[answer_raw] > wrong_avg * LENGTH_RATIO_THRESHOLD and lens[answer_raw] > MIN_LENGTH_TO_CONSIDER:
            split = find_dash_split(correct)
            if split:
                core, _tail = split
                options[answer_raw] = core
                stats['trimmed'] += 1
                changed = True
            else:
                stats['left_long_no_dash'] += 1

        new_options_json = '[' + ','.join(json.dumps(o, ensure_ascii=False) for o in options) + ']'
        return '{q:' + q_raw + ', options:' + new_options_json + ', answer:' + str(answer_raw) + '}'

    new_text = Q_OBJ.sub(repl, text)
    if changed and not dry_run:
        open(path, 'w', encoding='utf-8').write(new_text)
    return stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--grade', type=int, default=None)
    args = parser.parse_args()

    grades = [args.grade] if args.grade is not None else list(range(13))
    for g in grades:
        path = os.path.join(DATA_DIR, f'grade{g}.ts')
        if not os.path.exists(path):
            continue
        stats = process_file(path, args.dry_run)
        print(f'grade{g}: trimmed {stats["trimmed"]} | left as-is (no clean dash split) {stats["left_long_no_dash"]}')


if __name__ == '__main__':
    main()
