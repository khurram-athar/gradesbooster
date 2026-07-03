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

Safe to re-run: any entry that already has a videoUrl is left untouched
and skipped, so this can be run once a day to slowly work through the
YouTube Data API's free quota (10,000 units/day; search.list costs 100
units per call, so ~100 lookups/day by default) until every grade is
covered. Re-running tomorrow continues automatically where today left off
-- no separate progress file needed, the .ts files themselves are the
record of what's done.

Usage:
  export YOUTUBE_API_KEY=your_key_here
  python3 fetch_video_ids.py                 # spend up to 90 lookups
  python3 fetch_video_ids.py --limit 50      # spend up to 50 lookups
  python3 fetch_video_ids.py --dry-run       # show what would be looked up, no API calls, no writes
  python3 fetch_video_ids.py --grade 3       # only process grade3.ts

No third-party dependencies -- uses only the Python standard library.
"""
import os
import re
import sys
import json
import argparse
import urllib.request
import urllib.parse
import urllib.error

API_KEY = os.environ.get('YOUTUBE_API_KEY')
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
MAX_DAYS = 30

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


def search_video(query):
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 1,
        'safeSearch': 'strict',
        'videoEmbeddable': 'true',
        'relevanceLanguage': 'en',
        'key': API_KEY,
    }
    url = f'{SEARCH_URL}?{urllib.parse.urlencode(params)}'
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read().decode())
    items = data.get('items', [])
    if not items:
        return None
    return items[0]['id']['videoId']


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

        query = f'{title} {gradestr(grade)} {subject} educational'
        if dry_run:
            remaining[0] -= 1
            print(f'    [dry-run] grade{grade} day{day} "{title}" ({subject}) -> would search: {query}')
            return m.group(0)

        try:
            vid = search_video(query)
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

    # Breadth-first: Day 1 across every grade, then Day 2 across every grade, etc.
    for day in range(1, MAX_DAYS + 1):
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

    if not args.dry_run:
        for g, entry in chunks_by_grade.items():
            if entry['changed']:
                open(entry['path'], 'w', encoding='utf-8').write(''.join(entry['chunks']))

    spent = args.limit - remaining[0]
    print(f'\nDone. {"Would look up" if args.dry_run else "Looked up"} {spent} videos this run (limit was {args.limit}).')
    if not args.dry_run:
        print('Re-run tomorrow (quota resets daily) to continue where this run left off.')


if __name__ == '__main__':
    main()
