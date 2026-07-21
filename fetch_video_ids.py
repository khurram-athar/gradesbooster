#!/usr/bin/env python3
"""
Fetch one real, topic-relevant YouTube video ID per curriculum lesson via
the YouTube Data API v3 search endpoint, and write it into that subject's
`videoUrl` field (data/gradeN.ts). Once videoUrl is set, app/learn/page.tsx
embeds that exact video instead of falling back to a live multi-result
YouTube search embed.

Fill order is BREADTH-FIRST ACROSS GRADES, not grade-by-grade: this run
fills every grade's Day 1 videos first (all 4 subjects, grade 0 through
12), then every grade's Day 2, and so on. Kids on any grade start on
Day 1, so Day 1 having a working video everywhere matters more than one
grade being 100% done while others haven't started. (Previously this
script exhausted grade 0 completely before touching grade 1, which could
leave later grades' Day 1 without a video for a long time.)

Day range is NOT hardcoded -- it's read from however many days each
grade{N}.ts file actually has, so this keeps working unchanged as Phase 3
adds days 31, 32, ... 187 to each grade over time. No re-editing this
script is needed as the curriculum grows; just keep running it.

Safe to re-run: any entry that already has a videoUrl is left untouched
and skipped, so this can be run once a day to slowly work through the
YouTube Data API's free quota (10,000 units/day; search.list costs 100
units per call, so ~100 lookups/day by default) until every grade is
covered. Re-running tomorrow continues automatically where today left off
-- no separate progress file needed, the .ts files themselves are the
record of what's done.

After writing .ts changes, this also regenerates data/gradeN.json for any
grade that changed (via build_json.py) -- the live site's curriculum sync
only ever reads .json, never .ts, so skipping this step would mean today's
newly-fetched videos sit in .ts and never actually reach production. Pass
--skip-json-rebuild to opt out (e.g. if you want to review .ts changes
before they're reflected in .json).

Usage:
  export YOUTUBE_API_KEY=your_key_here
  python3 fetch_video_ids.py                 # spend up to 90 lookups, then rebuild changed .json files
  python3 fetch_video_ids.py --limit 50      # spend up to 50 lookups
  python3 fetch_video_ids.py --dry-run       # show what would be looked up, no API calls, no writes
  python3 fetch_video_ids.py --grade 3       # only process grade3.ts
  python3 fetch_video_ids.py --skip-json-rebuild   # update .ts only, don't touch .json

No third-party dependencies -- uses only the Python standard library.
(build_json.py, invoked automatically at the end, does shell out to `npx
tsx`, but that's its concern, not this script's.)
"""
import os
import re
import sys
import json
import argparse
import subprocess
import urllib.request
import urllib.parse
import urllib.error

API_KEY = os.environ.get('YOUTUBE_API_KEY')
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

# 2026-07-20: a Grade 7 parent reported that the Social Studies Day 3 video
# ("Physical Patterns in a Changing World") was an unrelated Hindi-language
# video about NCERT textbook changes. Root cause: search_video() always
# accepted YouTube's #1 result with no check on title/channel language or
# topical relevance, and the query embedded the raw camelCase subject key
# (e.g. "SocialStudies") instead of a readable label, which weakened
# match quality. Generic "grade N <subject>" queries are dominated by
# high-volume Indian CBSE/NCERT/ICSE "Class N" content on YouTube, so
# without a filter, that's often what search.list's top result actually is.
#
# Fixes below: readable subject labels in the query, a banned-keyword
# filter on title+description (catches CBSE/NCERT/ICSE/board-exam/Hindi
# and similar off-curriculum content), a regionCode hint, and multiple
# candidates scored by keyword overlap with the lesson title instead of
# blindly trusting result #1. If nothing passes the filter, we leave
# videoUrl blank and let a future run try again rather than write a risky
# guess -- a missing video (falls back to a live search embed) is a much
# smaller problem than a wrong, non-English video playing for a kid.
SUBJECT_LABELS = {
    'SocialStudies': 'Social Studies',
    'AdvancedFunctions': 'Advanced Functions',
}

BANNED_KEYWORDS = [
    'ncert', 'cbse', 'icse', 'board exam', 'boards exam', 'entrance exam',
    'jee', 'neet', 'upsc', 'ssc', 'byju', 'hindi medium', 'हिंदी', 'हिन्दी',
    'में पढ़ें', 'class 6th', 'class 7th', 'class 8th', 'class 9th', 'class 10th',
    'class 11th', 'class 12th', "what's changed", 'must watch',
]

STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'of', 'in', 'on', 'to', 'for', 'with',
    'is', 'are', 'part', 'introduction', 'review', 'grade', 'educational',
}


def readable_subject(subject):
    return SUBJECT_LABELS.get(subject, subject)


def is_banned(text):
    lowered = text.lower()
    return any(term in lowered for term in BANNED_KEYWORDS)


def relevance_score(lesson_title, candidate_title):
    lesson_words = {w for w in re.findall(r"[a-z']+", lesson_title.lower()) if w not in STOPWORDS and len(w) > 2}
    candidate_words = {w for w in re.findall(r"[a-z']+", candidate_title.lower())}
    if not lesson_words:
        return 0
    return len(lesson_words & candidate_words)

# Splits a whole file into: [header_before_day1, day1_block_text, day2_block_text, ...]
# Each day_block_text starts at "{day:N," and runs up to (not including) the next "{day:".
DAY_SPLIT_RE = re.compile(r'(?=\{day:\d+,)')

# Each subject block looks like:
#   {subject:"Math", title:"Multiplication Facts", summary:"...",
#    resourceLabel:"YouTube: ...", resourceUrl:"https://...",
#    videoUrl:"https://www.youtube.com/watch?v=XXXXXXXXXXX",   <- optional, what we add
#    quiz:[
BLOCK_RE = re.compile(
    r'(\{subject:"([^"]+)", title:"([^"]+)",.*?\n\s*resourceLabel:"[^"]*", resourceUrl:"[^"]*",\n)'
    r'(\s*videoUrl:"[^"]*",\n)?',
    re.DOTALL,
)


def gradestr(g):
    return 'kindergarten' if g == 0 else f'grade {g}'


def search_video(query, lesson_title):
    """Fetches several candidates (not just #1), drops anything matching a
    banned keyword in its title/description or channel name, then returns
    the surviving candidate whose title shares the most keywords with the
    lesson title. Returns None if nothing passes -- callers should leave
    videoUrl blank rather than accept a low-confidence match."""
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 8,
        'safeSearch': 'strict',
        'videoEmbeddable': 'true',
        'relevanceLanguage': 'en',
        'regionCode': 'CA',
        'key': API_KEY,
    }
    url = f'{SEARCH_URL}?{urllib.parse.urlencode(params)}'
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read().decode())
    items = data.get('items', [])

    candidates = []
    for item in items:
        snippet = item.get('snippet', {})
        title = snippet.get('title', '')
        description = snippet.get('description', '')
        channel = snippet.get('channelTitle', '')
        if is_banned(title) or is_banned(description) or is_banned(channel):
            continue
        score = relevance_score(lesson_title, title)
        if score == 0:
            continue
        candidates.append((score, item['id']['videoId'], title))

    if not candidates:
        return None
    candidates.sort(key=lambda c: c[0], reverse=True)
    return candidates[0][1]


def load_day_chunks(path):
    """Returns a list where chunks[0] is everything before day 1's block,
    and chunks[N] (for N >= 1) is day N's full block text (if that many
    days exist in the file)."""
    text = open(path, encoding='utf-8').read()
    return DAY_SPLIT_RE.split(text)


def process_day_chunk(chunk, grade, day, remaining, dry_run):
    """Fills missing videoUrl fields within a single day's block text.
    Returns (new_chunk_text, changed_bool)."""
    changed = False

    def repl(m):
        nonlocal changed
        prefix, subject, title, existing_video = m.group(1), m.group(2), m.group(3), m.group(4)
        if existing_video:
            return m.group(0)
        if remaining[0] <= 0:
            return m.group(0)

        query = f'{title} {gradestr(grade)} {readable_subject(subject)} educational'
        if dry_run:
            remaining[0] -= 1
            print(f'    [dry-run] grade{grade} day{day} "{title}" ({subject}) -> would search: {query}')
            return m.group(0)

        try:
            vid = search_video(query, title)
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors='replace')
            print(f'    ERROR grade{grade} day{day} "{title}": HTTP {e.code} {body[:200]}', file=sys.stderr)
            if e.code == 403:
                # Quota exceeded or key restricted -- stop burning attempts this run.
                remaining[0] = 0
            return m.group(0)
        except Exception as e:
            print(f'    ERROR grade{grade} day{day} "{title}": {e}', file=sys.stderr)
            return m.group(0)

        remaining[0] -= 1
        if not vid:
            print(f'    no result for grade{grade} day{day} "{title}"')
            return m.group(0)

        changed = True
        print(f'    grade{grade} day{day} "{title}" -> https://www.youtube.com/watch?v={vid}  ({remaining[0]} lookups left this run)')
        return f'{prefix}   videoUrl:"https://www.youtube.com/watch?v={vid}",\n'

    new_chunk = BLOCK_RE.sub(repl, chunk)
    return new_chunk, changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=90, help='max API searches to spend this run (default 90)')
    parser.add_argument('--grade', type=int, default=None, help='only process this grade (0-12)')
    parser.add_argument('--dry-run', action='store_true', help="show what would be searched, don't call the API or write files")
    parser.add_argument('--skip-json-rebuild', action='store_true', help="update .ts only; don't regenerate .json for changed grades")
    args = parser.parse_args()

    if not args.dry_run and not API_KEY:
        print('Set YOUTUBE_API_KEY in your environment first, e.g.:', file=sys.stderr)
        print('  export YOUTUBE_API_KEY=your_key_here', file=sys.stderr)
        sys.exit(1)

    grades = [args.grade] if args.grade is not None else list(range(13))
    remaining = [args.limit]

    # Load every grade file's day-chunks once up front.
    chunks_by_grade = {}
    for g in grades:
        path = os.path.join(DATA_DIR, f'grade{g}.ts')
        if not os.path.exists(path):
            continue
        chunks_by_grade[g] = {'path': path, 'chunks': load_day_chunks(path), 'changed': False}

    # Day range is per-grade, not a shared constant: chunks[0] is the file
    # header (everything before "{day:1,"), so chunks[1:] are the actual
    # day blocks -- len(chunks) - 1 is exactly how many days that grade
    # currently has, whether that's 30 (today) or 187 (once Phase 3 is
    # fully built out). max_day below is just "the longest any grade goes
    # this run" so the breadth-first loop below covers every grade present.
    max_day = max((len(entry['chunks']) - 1 for entry in chunks_by_grade.values()), default=0)

    # Breadth-first: Day 1 across every grade, then Day 2 across every grade, etc.
    for day in range(1, max_day + 1):
        if remaining[0] <= 0:
            break
        for g in grades:
            if remaining[0] <= 0:
                break
            entry = chunks_by_grade.get(g)
            if entry is None or day >= len(entry['chunks']):
                continue  # this grade doesn't have this many days
            new_chunk, changed = process_day_chunk(entry['chunks'][day], g, day, remaining, args.dry_run)
            if changed:
                entry['chunks'][day] = new_chunk
                entry['changed'] = True

    changed_grades = []
    if not args.dry_run:
        for g, entry in chunks_by_grade.items():
            if entry['changed']:
                open(entry['path'], 'w', encoding='utf-8').write(''.join(entry['chunks']))
                changed_grades.append(g)

    spent = args.limit - remaining[0]
    print(f'\nDone. {"Would look up" if args.dry_run else "Looked up"} {spent} videos this run (limit was {args.limit}).')
    if args.dry_run:
        return

    if not changed_grades:
        print('No grade files changed -- nothing to rebuild.')
        return

    if args.skip_json_rebuild:
        print(f'{len(changed_grades)} grade(s) changed ({changed_grades}) -- .json NOT rebuilt (--skip-json-rebuild).')
        print('Remember to run build_json.py before pushing, or the site will never see these videos.')
        return

    print(f'\nRegenerating .json for {len(changed_grades)} changed grade(s): {changed_grades}')
    build_json_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build_json.py')
    for g in changed_grades:
        result = subprocess.run(
            [sys.executable, build_json_script, '--grade', str(g)],
            capture_output=True, text=True,
        )
        print(result.stdout.strip())
        if result.returncode != 0:
            print(f'  WARNING: build_json.py failed for grade{g}:\n{result.stderr}', file=sys.stderr)

    print('\nDone. If this looks right, commit + push data/*.ts and data/*.json,')
    print('then trigger a curriculum sync so Supabase (and the live site) picks it up.')


if __name__ == '__main__':
    main()
