#!/usr/bin/env python3
"""
Rebalance the position of the correct answer across every quiz question in
data/gradeN.ts. Question/option TEXT is never changed -- only which slot
(0-3) holds the correct answer, and the shuffled order of the wrong options.

Why: an audit found the correct answer was heavily clustered on one option
index in most grade files (e.g. grade9: 94% of answers were option A),
letting kids score well by button-position pattern-matching instead of
reading. This script fixes that by assigning each question's correct-answer
slot via a shuffled round-robin (exactly even across 0/1/2/3 per file) and
randomly permuting the wrong options into the remaining slots.

Usage:
  python3 fix_answer_bias.py --dry-run          # report only, no writes
  python3 fix_answer_bias.py                    # apply to all grade files
  python3 fix_answer_bias.py --grade 5           # only grade5.ts
"""
import re
import json
import random
import argparse
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

STR = r'"(?:[^"\\]|\\.)*"'
OPTIONS = r'\[\s*' + STR + r'(?:\s*,\s*' + STR + r')*\s*\]'
Q_OBJ = re.compile(r'\{q:(' + STR + r'), options:(' + OPTIONS + r'), answer:(\d+)\}')


def process_file(path, seed, dry_run):
    random.seed(seed)
    text = open(path, encoding='utf-8').read()
    matches = list(Q_OBJ.finditer(text))
    n = len(matches)
    if n == 0:
        return 0, {}

    targets = [i % 4 for i in range(n)]
    random.shuffle(targets)

    out = []
    last_end = 0
    new_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for idx, m in enumerate(matches):
        q_raw, options_raw, answer_raw = m.group(1), m.group(2), int(m.group(3))
        options = json.loads(options_raw)
        if len(options) != 4:
            # Leave anything non-standard untouched.
            out.append(text[last_end:m.end()])
            last_end = m.end()
            continue
        correct_text = options[answer_raw]
        wrong_texts = [o for i, o in enumerate(options) if i != answer_raw]
        random.shuffle(wrong_texts)
        target = targets[idx]
        new_options = wrong_texts[:]
        new_options.insert(target, correct_text)
        new_counts[target] += 1

        new_options_json = '[' + ','.join(json.dumps(o, ensure_ascii=False) for o in new_options) + ']'
        new_q_json = q_raw  # q text untouched, reuse raw original literal
        replacement = '{q:' + new_q_json + ', options:' + new_options_json + ', answer:' + str(target) + '}'

        out.append(text[last_end:m.start()])
        out.append(replacement)
        last_end = m.end()

    out.append(text[last_end:])
    new_text = ''.join(out)

    if not dry_run:
        open(path, 'w', encoding='utf-8').write(new_text)

    return n, new_counts


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
        n, counts = process_file(path, seed=1000 + g, dry_run=args.dry_run)
        if n == 0:
            print(f'grade{g}: no quiz questions found')
            continue
        pct = {k: round(v / n * 100) for k, v in counts.items()}
        print(f'grade{g}: n={n} new distribution -> ' + ' '.join(f'{k}:{v}%' for k, v in pct.items()))


if __name__ == '__main__':
    main()
