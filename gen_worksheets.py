#!/usr/bin/env python3
"""Shared helpers for generating GradesBooster standalone worksheet data
files (data/gradeN_worksheets.ts), mirroring the conventions of
gen_curriculum.py for the day-based lesson files.

This is a NEW, separate data pipeline from data/gradeN.ts (day-based
lessons). Worksheets are supplementary practice material, not part of the
187-day sequence, and don't need a videoUrl/resourceLabel/resourceUrl --
they're pure question sets, optionally printable.

Scope per Project Plan item 8 (confirmed 2026-08-20): 10 worksheets per
subject per grade, 13 grades, exactly 15 questions per worksheet -- 520
worksheets, 7,800 questions total.

Question format (mixed by grade band, confirmed 2026-08-20):
  - Kindergarten (grade 0) and Grade 1: free-response. Each question is a
    plain prompt string with no options/answer key, matching the existing
    style of the required 3-item K/1 daily worksheet field already
    embedded in gradeN.ts (that field is untouched by this new pipeline).
  - Grades 2-12: multiple choice, exactly 4 options + a 0-indexed answer,
    matching the existing daily quiz style.

No embedded straight double-quotes or apostrophes anywhere in title/q/
options text -- same rule as the day-based curriculum content. Drop
contractions/possessives entirely (e.g. "does not" not "doesnt", "Canadas"
not "Canada's").

This is a content-only pass: no in-app display feature/schema exists yet
for these files (that's separate, not-yet-scoped follow-on work), so the
.ts files intentionally have no `import type` line -- there's no
WorksheetContent type in the app's type system to import. Plain untyped
array literals are valid TS and import fine via tsx (see
build_worksheets_json.py).
"""
import os

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def mc(q, opts, a):
    """One multiple-choice question: q="prompt text", opts=[4 strings],
    a=0-indexed correct answer. Used for grades 2-12."""
    assert len(opts) == 4, f'expected exactly 4 options, got {len(opts)}: {q!r}'
    assert 0 <= a < 4, f'answer index {a} out of range for {q!r}'
    for text in [q] + opts:
        assert '"' not in text and "'" not in text, f'stray quote in: {text!r}'
    return ('mc', q, opts, a)


def fr(q):
    """One free-response question: q="prompt text" only, no answer key.
    Used for Kindergarten (grade 0) and Grade 1."""
    assert '"' not in q and "'" not in q, f'stray quote in: {q!r}'
    return ('fr', q)


def worksheet(subject, number, title, questions):
    """One worksheet: subject key (grade-specific, e.g. 'Math', 'History',
    'AdvancedFunctions'), number (1-10), title (distinct within this
    subject+grade), and exactly 15 questions (all mc() or all fr(), not
    mixed within one worksheet)."""
    assert len(questions) == 15, f'{title!r}: expected exactly 15 questions, got {len(questions)}'
    kinds = {q[0] for q in questions}
    assert len(kinds) == 1, f'{title!r}: mixed mc/fr question kinds in one worksheet'
    assert '"' not in title and "'" not in title, f'stray quote in title: {title!r}'
    return (subject, number, title, questions)


def _render_question(q):
    kind = q[0]
    if kind == 'fr':
        _, qtext = q
        return f'    {{q:"{qtext}"}}'
    _, qtext, opts, a = q
    opts_str = ','.join(f'"{o}"' for o in opts)
    return f'    {{q:"{qtext}", options:[{opts_str}], answer:{a}}}'


def _render_worksheet(w):
    subject, number, title, questions = w
    out = [f'{{subject:"{subject}", number:{number}, title:"{title}", questions:[']
    for i, q in enumerate(questions):
        sep = ',' if i < len(questions) - 1 else ''
        out.append(_render_question(q) + sep)
    out.append(']},')
    return '\n'.join(out)


def build(worksheets):
    out = ['const worksheets = [']
    for w in worksheets:
        out.append(_render_worksheet(w))
    out += ['];', '', 'export default worksheets;']
    return '\n'.join(out)


def write_worksheets(grade, worksheets):
    """Writes data/gradeN_worksheets.ts from scratch (this pipeline has no
    incremental append step -- each grade's full 40 worksheets, 4 subjects
    x 10, are written in one shot by that grade's gen_gradeN_worksheets.py)."""
    p = f'{DIR}/grade{grade}_worksheets.ts'
    open(p, 'w').write(build(worksheets))
    print(f'grade{grade}_worksheets.ts written ({len(worksheets)} worksheets)')
