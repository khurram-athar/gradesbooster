#!/usr/bin/env python3
"""
Fetch one real, topic-relevant YouTube video ID per curriculum lesson via
the YouTube Data API v3 search endpoint, and write it into that subject's
`videoUrl` field (data/gradeN.ts). Once videoUrl is set, app/learn/page.tsx
embeds that exact video instead of falling back to a live multi-result
YouTube search embed.

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


def process_file(path, grade, remaining, dry_run):
    text = open(path, encoding='utf-8').read()
    changed = False
    quota_hit = [False]

    def repl(m):
        nonlocal changed
        prefix, subject, title, existing_video = m.group(1), m.group(2), m.group(3), m.group(4)
        if existing_video:
            return m.group(0)
        if remaining[0] <= 0:
            quota_hit[0] = True
            return m.group(0)

        query = f'{title} {gradestr(grade)} {subject} educational'
        if dry_run:
            remaining[0] -= 1
            print(f'    [dry-run] grade{grade} "{title}" ({subject}) -> would search: {query}')
            return m.group(0)

        try:
            vid = search_video(query)
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors='replace')
            print(f'    ERROR grade{grade} "{title}": HTTP {e.code} {body[:200]}', file=sys.stderr)
            if e.code == 403:
                # Quota exceeded or key restricted -- stop burning attempts this run.
                remaining[0] = 0
                quota_hit[0] = True
            return m.group(0)
        except Exception as e:
            print(f'    ERROR grade{grade} "{title}": {e}', file=sys.stderr)
            return m.group(0)

        remaining[0] -= 1
        if not vid:
            print(f'    no result for grade{grade} "{title}"')
            return m.group(0)

        changed = True
        print(f'    grade{grade} "{title}" -> https://www.youtube.com/watch?v={vid}  ({remaining[0]} lookups left this run)')
        return f'{prefix}   videoUrl:"https://www.youtube.com/watch?v={vid}",\n'

    new_text = BLOCK_RE.sub(repl, text)
    if changed and not dry_run:
        open(path, 'w', encoding='utf-8').write(new_text)
    return changed


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

    for g in grades:
        if remaining[0] <= 0:
            break
        path = os.path.join(DATA_DIR, f'grade{g}.ts')
        if not os.path.exists(path):
            continue
        print(f'grade{g}.ts...')
        process_file(path, g, remaining, args.dry_run)

    spent = args.limit - remaining[0]
    print(f'\nDone. {"Would look up" if args.dry_run else "Looked up"} {spent} videos this run (limit was {args.limit}).')
    if not args.dry_run:
        print('Re-run tomorrow (quota resets daily) to continue where this run left off.')


if __name__ == '__main__':
    main()
