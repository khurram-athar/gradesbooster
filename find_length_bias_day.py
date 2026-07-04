#!/usr/bin/env python3
"""
Find remaining answer-length-bias questions in a specific Day block, across
all grade files. This is the manual-review counterpart to fix_answer_length_bias.py:
that script already trimmed every case with a clean em-dash split, file-wide.
What's left needs a human (or Claude) to rewrite by hand, day by day,
breadth-first across grades, per the existing project convention.

Usage:
  python3 find_length_bias_day.py --day 4
  python3 find_length_bias_day.py --day 4 --grade 5
"""
import re
import json
import argparse
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

STR = r'"(?:[^"\\]|\\.)*"'
OPTIONS = r'\[\s*' + STR + r'(?:\s*,\s*' + STR + r')*\s*\]'
Q_OBJ = re.compile(r'\{q:(' + STR + r'), options:(' + OPTIONS + r'), answer:(\d+)\}')
DAY_HEADER = re.compile(r'\{day:(\d+),')

LENGTH_RATIO_THRESHOLD = 1.8
MIN_LENGTH_TO_CONSIDER = 40


def get_day_block(text, day):
    """Return the substring of text covering {day:N,...} up to next {day: or EOF."""
    starts = [(m.start(), int(m.group(1))) for m in DAY_HEADER.finditer(text)]
    for i, (pos, d) in enumerate(starts):
        if d == day:
            end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
            return text[pos:end]
    return None


def scan_day(path, day):
    text = open(path, encoding='utf-8').read()
    block = get_day_block(text, day)
    if block is None:
        return []
    flagged = []
    for m in Q_OBJ.finditer(block):
        q_raw, options_raw, answer_raw = m.group(1), m.group(2), int(m.group(3))
        options = json.loads(options_raw)
        if len(options) != 4:
            continue
        lens = [len(o) for o in options]
        wrong_avg = sum(l for i, l in enumerate(lens) if i != answer_raw) / 3
        if wrong_avg == 0:
            continue
        if lens[answer_raw] > wrong_avg * LENGTH_RATIO_THRESHOLD and lens[answer_raw] > MIN_LENGTH_TO_CONSIDER:
            flagged.append({
                'q': json.loads(q_raw),
                'options': options,
                'answer': answer_raw,
                'ratio': round(lens[answer_raw] / wrong_avg, 2),
            })
    return flagged


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', type=int, required=True)
    parser.add_argument('--grade', type=int, default=None)
    args = parser.parse_args()

    grades = [args.grade] if args.grade is not None else list(range(13))
    total = 0
    for g in grades:
        path = os.path.join(DATA_DIR, f'grade{g}.ts')
        if not os.path.exists(path):
            continue
        flagged = scan_day(path, args.day)
        if flagged:
            print(f'=== grade{g} day{args.day}: {len(flagged)} flagged ===')
            for f in flagged:
                print(f'  ratio={f["ratio"]}  answer={f["answer"]}')
                print(f'    q: {f["q"]}')
                for i, o in enumerate(f['options']):
                    mark = '  <-- ANSWER' if i == f['answer'] else ''
                    print(f'    [{i}] ({len(o)} chars) {o}{mark}')
            total += len(flagged)
        else:
            print(f'grade{g} day{args.day}: clean')
    print(f'\nTOTAL flagged: {total}')


if __name__ == '__main__':
    main()
