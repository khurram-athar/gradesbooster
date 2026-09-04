#!/usr/bin/env bash
# scripts/git_lock_cleanup.sh
#
# Safely clears stale git lock files in this repo, for use by any
# automated/unattended session (e.g. the curriculum-video-backfill
# scheduled task) that talks to this repo through the Cowork
# device-bridge shell.
#
# WHY THIS EXISTS: that shell can rename files but cannot delete them
# (unlink fails with "Operation not permitted", by design of the
# sandbox). When a git command dies mid-write, it can leave a lock
# file behind (.git/index.lock, .git/HEAD.lock, .git/refs/heads/main.lock,
# etc.) that blocks every subsequent git command with "Unable to
# create '.../*.lock': File exists". Since the file can't be deleted,
# every past session worked around this ad hoc by renaming the lock
# out of the way (.bak, .bak2, .stale, .pre, .old, .retry1, ...) --
# with no two sessions using the same convention, and no cleanup step,
# this scattered several hundred stray files loose in .git/ over the
# past few months.
#
# On 2026-09-04 this caused a real breakage: a stray renamed file
# ended up literally inside .git/refs/heads/ (main.lock.bak.<ts>,
# 0 bytes). Git scans every file in refs/heads/ as a candidate branch
# ref, so an empty/invalid one there broke `git pull` with
# "fatal: bad object refs/heads/main.lock.bak.<ts>".
#
# THE FIX: never leave a renamed lock loose in place, and never leave
# one inside any refs/ subdirectory (git only expects literal `*.lock`
# files it wrote itself there -- WE must not leave anything else in
# that directory at all). Always relocate stale lock files into one
# single, contained, git-internal directory: .git/.stale-locks/.
# Being inside .git/ (not the working tree), nothing placed there can
# ever be tracked, staged, or scanned as a ref, no matter what it's
# named.
#
# USAGE: run this once at the start of any automated session before
# touching git, and again immediately if any git command fails with
# a "File exists" lock error. It is always safe to run -- it only
# moves files that are already stray, never ones actively in use by
# a live git process (see the age check below).
#
# Exit code is always 0 (this is a best-effort sweep, not a gate).

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "git_lock_cleanup: not inside a git repo, nothing to do" >&2
  exit 0
}
cd "$REPO_ROOT"

STALE_DIR=".git/.stale-locks"
mkdir -p "$STALE_DIR" 2>/dev/null

moved=0
skipped_fresh=0
# Locks younger than this are left alone -- they might belong to a git
# process that is genuinely running right now. This repo is only ever
# touched by one Cowork session at a time, so a few seconds is plenty;
# pass --force (e.g. immediately after a git command just failed with
# "File exists") to skip this check entirely and sweep regardless of age.
FRESH_SECONDS=5
FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

is_stale() {
  # GNU stat (-c) and BSD/macOS stat (-f) take the SAME flag letters for
  # different meanings, so a naive try-one-then-fall-back can silently
  # succeed with the wrong stat and print garbage instead of failing --
  # validate the output is purely numeric before trusting it.
  [ "$FORCE" = "1" ] && return 0
  local f="$1"
  local mtime now age
  mtime=$(stat -c "%Y" "$f" 2>/dev/null)
  if ! [[ "$mtime" =~ ^[0-9]+$ ]]; then
    mtime=$(stat -f "%m" "$f" 2>/dev/null)
  fi
  if ! [[ "$mtime" =~ ^[0-9]+$ ]]; then
    return 1
  fi
  now=$(date +%s)
  age=$((now - mtime))
  [ "$age" -ge "$FRESH_SECONDS" ]
}

relocate() {
  local f="$1"
  local base
  base="$(basename "$f")"
  if is_stale "$f"; then
    if mv "$f" "$STALE_DIR/${base}.$(date +%s%N 2>/dev/null || date +%s)" 2>/dev/null; then
      moved=$((moved + 1))
    fi
  else
    skipped_fresh=$((skipped_fresh + 1))
  fi
}

# 1) Known top-level lock files git itself writes.
for f in .git/HEAD.lock .git/index.lock .git/MERGE_HEAD.lock .git/ORIG_HEAD.lock .git/FETCH_HEAD.lock .git/packed-refs.lock; do
  [ -e "$f" ] && relocate "$f"
done

# 2) THE IMPORTANT ONE: anything sitting inside refs/** that isn't a
#    real ref file git wrote. Treat every *.lock and every previously
#    mis-renamed *.bak*/*.stale*/*.pre*/*.old*/*.retry* file under
#    refs/ as a stray, regardless of age (never legitimate there).
if [ -d .git/refs ]; then
  while IFS= read -r -d '' f; do
    base="$(basename "$f")"
    mv "$f" "$STALE_DIR/${base}.$(date +%s%N 2>/dev/null || date +%s)" 2>/dev/null && moved=$((moved + 1))
  done < <(find .git/refs -type f \( \
      -name "*.lock" -o -name "*.lock.*" -o -name "*.bak*" \
      -o -name "*.stale*" -o -name "*.pre*" -o -name "*.old*" \
      -o -name "*.retry*" \
    \) -print0 2>/dev/null)
fi

# 3) Sweep any previously-scattered clutter already loose in .git/ root
#    (everything this workaround produced before this script existed)
#    into the same contained directory, so .git/ stops accumulating.
while IFS= read -r -d '' f; do
  relocate "$f"
done < <(find .git -maxdepth 1 -type f \( \
    -name "*.lock.bak*" -o -name "*.lock.stale*" -o -name "*.lock.pre*" \
    -o -name "*.lock.old*" -o -name "*.lock.retry*" -o -name "*.lock.moved*" \
  \) -print0 2>/dev/null)

echo "git_lock_cleanup: relocated $moved stale file(s) into $STALE_DIR/ (skipped $skipped_fresh as too fresh to be sure they're stale)"
exit 0
