# Days 1-30 Video Audit — Working Backlog

**Status: superseded the two prior report files as the authoritative worklist for the automated `curriculum-video-backfill` task's Days 1-30 phase (added 2026-08-20).** `grades_5_12_video_audit_report.md` (2026-07-21) and `video_audit_status_eod.md` (2026-07-22) are kept for historical reference/detail (some entries below cite them for original phrasing) but are otherwise frozen — update THIS file going forward as items get verified/fixed.

**Why this file exists:** the original July 21-22 audit never finished (agents kept hitting the shared YouTube search quota mid-pass), and `curriculum-video-backfill`'s SKILL.md previously and incorrectly claimed Days 1-30 were "fully audited... every video confirmed relevant" for all grades. That claim is false. Worse, Grade 7 was marked "complete, all issues fixed" on 2026-07-22, yet a real mismatch (Day 5 SocialStudies — a single generic "Regions of Canada" video attached to a review lesson actually covering New France/Seven Years War, the Rebellions of 1837-38, climate zones, and natural resources) was found and fixed manually on 2026-08-20, undetected by that "complete" audit. **Treat every "fully checked"/"complete" label below with some skepticism — verify, don't just trust the label.**

**How to use this file (for the automated task):** work grades top-to-bottom in the priority order below. Within a grade, work its "Confirmed bad — needs fix" list first (these don't need re-verification of the problem itself, just look up the day/subject's CURRENT videoUrl in `data/gradeN.json` since content may have shifted since July, then search+replace per the normal Step 2-4 process). Then work its "Ambiguous — needs judgment call" list (quick re-check: is the current video actually fine, or does it need replacing? use judgment, same quality bar as Step 3). Then, if budget remains, spot-check a handful of that grade's "Unchecked/unverified" days before moving to the next grade. Check items off (strike through or mark `[x] FIXED <date> <new videoId>` / `[x] VERIFIED OK <date>` / `[x] MOOT <date> <reason>`) as you resolve them — this file is the persistent progress record across runs, since (unlike Day 31+ missing-video detection) "already has a videoUrl" does NOT mean "already correct" for these lessons, so there's no way to derive backlog state from the JSON alone.

**Grade priority order** (worst-known-coverage / highest-known-issue-count first, per the original report's own recommendation, with Grade 7 inserted for re-verification given the slip-through):

1. Grade 10 — fully classified in July, ZERO fixes applied (quota died every time)
2. Grade 12 — fully classified, ZERO fixes applied (quota died on first search)
3. Grade 9 — 4 fixed in July, ~20 confirmed-bad still outstanding
4. Grade 11 — 5 fixed in July, ~15 confirmed-bad still outstanding
5. Grade 5 — only ~35% ever checked, 4 fixed, most of the grade never even looked at
6. Grade 6 — only ~27% ever checked, 2 fixed
7. Grade 8 — ~64% checked, 0 fixes applied despite being fully classified
8. Grade 7 — marked "complete" in July but proven unreliable (2026-08-20 slip-through) — full independent re-verification pass, not just trusting old status
9. Grades 0-4 — previously audited AND fixed (Grade 0: 15 fixes, Grade 1: 17, Grade 2: 13, Grade 3: 7, Grade 4: 2 partial + 9 "too-long" flags that are likely non-issues under the current too-long-is-fine policy) — lowest priority, spot-check only, given the Grade 7 lesson learned that "done" claims deserve a light trust-but-verify pass eventually

---

## 1. Grade 10 — HIGHEST PRIORITY

**Confirmed bad — needs fix (34 total):**
- [ ] Day 9, English ("Novel Study: Contemporary Canadian Novel") — UK GCSE video, wrong curriculum
- [ ] Day 12, English ("Poetry — Voice, Identity, and Social Justice") — random amateur student poem, unrelated
- [ ] `zz440EuFK8Q` ("The history of Canada explained in 10 minutes," a generic overview) reused 8x in the History slot — confirmed via oembed. Fix EACH of these 8 individually with a lesson-specific video: Day 2, Day 5, Day 6, Day 10, Day 12, Day 17, Day 21, Day 24 (all History)
- [ ] 5 blocks with NO videoUrl at all: Day 28 History, and all of Day 30 (English, Math, Science, History)
- [ ] 19 more spread across Days 11, 15, 16, 18, 19 (x2 — two subjects that day), 20, 22, 23, 24, 25, 26, 27, 28 — wrong-country history videos, elementary-level content, banned-keyword (CBSE/BYJU) hits, clickbait, topic mismatches. Exact subject/title not preserved from the original report — look up each day's full lesson set in `data/grade10.json`, re-run the oembed/snippet free check on every Day 1-30 History/English/Math/Science block for this grade to identify which specific ones are still bad (the 8x-reused ID and the 2 named above are already confirmed; the remaining ~19 need a fresh title/description pull to pinpoint).

**Ambiguous — needs judgment call (10 total):**
- [ ] Days 3, 5, 7, 10, 14, 16, 17, 20, 21, 28 — mostly right-general-topic-but-wrong-angle or wrong-country videos flagged in July; re-check each against current lesson content and decide keep/replace.

**Unchecked/unverified:** none — Grade 10 was 100% checked (topic-relevance) in July, this list above IS the full known-issue set. Duration was also checked in the same pass.

---

## 2. Grade 12

**Confirmed bad — needs fix (20 total):**
- [ ] Days 2, 10 (x2), 12, 13, 15 (x3), 16, 20, 21, 22, 23, 25, 28, 29 (x2), 30 (x3 — includes 2 dead/404 videos, so at least 2 of Day 30's blocks have literally broken links, priority-fix these first)

**Ambiguous — needs judgment call (14 total):**
- [ ] Days 2, 3, 5, 6, 9, 11, 13, 14, 15, 24 (x2), 26, 28, 29

**Unchecked/unverified:** none reported — treat as fully classified, same caveat as Grade 10 about exact subject/title not preserved from the prose report; re-pull current title/description per flagged day via free oembed/snippet call before searching for a replacement.

---

## 3. Grade 9

**Already fixed 2026-07-21 (verify these are still good, don't re-spend budget unless verification fails):**
- [x] Day 5, SocialStudies ("Review: Geography and Resources") — fixed to a Natural Resources in Canada (CGC1W) video
- [x] Day 6, SocialStudies ("Careers Related to Geography") — fixed to a geography-careers-specific video
- [x] Day 27, SocialStudies ("Geography of Public Health and Disease Spread") — fixed to Crash Course Geography's "How Does Disease Move?"
- [x] Day 29, SocialStudies ("Geographic Inquiry Project Design") — fixed to an Ontario Teachers' Federation geo-inquiry video

**Confirmed bad — needs fix (~20 total, mostly elementary-level "Dr Binocs"/"Rock N Learn" content, UK GCSE videos, one Hindi-language video):**
- [ ] Days 1, 2, 6, 7, 9, 10, 13, 15 (x3), 19, 20 (x3), 23, 24, 25, 26, 28

**Ambiguous — needs judgment call (10 total):**
- [ ] Days 5, 7, 9, 12, 18, 21 (x2), 26, 29 (x2)

---

## 4. Grade 11

**Already fixed 2026-07-21 (verify still good):**
- [x] Day 16, English ("Dystopian Fiction and Social Critique") — fixed to a video on Orwell's dystopian fiction and social criticism
- [x] Day 18, English ("Social Realism in Literature") — fixed to an English-language literary-movements video on Realism
- [x] Day 19, Functions ("Graphing Technology") — fixed to an MCR3U graphing-with-transformations overview
- [x] Day 20, Biology ("Human Reproduction: Reproductive Technologies") — fixed to TED-Ed's IVF explainer
- [x] Day 23, Biology ("Reproductive System and Development Review") — fixed to a reproductive-system-specific video

**Confirmed bad — needs fix (~15 total, clickbait Shorts, wrong-subject videos, generic study-tips content):**
- [ ] Days 13, 14, 15, 20, 21, 22, 24 (x2), 25, 26, 27 (x2), 29 (x3)

**Ambiguous — needs judgment call (18 total):**
- [ ] Days 1, 2, 6, 7 (x2), 8, 10, 11, 12, 13, 14, 15, 20, 22 (x2), 23, 25 (x2), 26, 29

---

## 5. Grade 5 — only ~35% ever checked

**Already fixed 2026-07-21/22 (4 total, verify still good):** exact days not preserved from the eod summary line — spot-check broadly since this grade's fix list wasn't itemized.

**Confirmed bad — needs fix:**
- [ ] Day 1, Math — clickbait Short "Did you know this trick?" — not real content
- [ ] Day 6, SocialStudies — "Alberta Social Studies 9" video (wrong grade AND wrong province) for "Canadian Citizenship and Identity"
- [ ] Day 16, SocialStudies — "Levels of Government" video reused for a Territories/geography lesson
- [ ] Day 26, Science — a Grade 4 Social Studies video used for "Renewable vs. Non-Renewable Resources" (wrong subject entirely)
- [ ] Day 30 (all 4 subjects) — no videoUrl at all, genuine gap
- [ ] ~15 more issues (duration outliers + a few mismatches) across Days 6, 7, 9, 10, 15, 17, 20, 21, 22, 23, 25 per the eod summary — not individually itemized, needs a fresh per-day check

**Ambiguous — needs judgment call:**
- [ ] Day 3 Science, Day 4 Science, Day 7 SocialStudies, Day 8 Math, Day 15 Math, Day 20 Math, Day 21 SocialStudies, Day 24 SocialStudies, Day 25 Math — each covers only part of a multi-topic lesson/review day
- [ ] 16 more ambiguous flags per the eod summary, days not individually itemized

**Unchecked/unverified:** Days 10, 11, 13, 14, 17, 18, 27 entirely, plus partial gaps elsewhere — lowest-confidence grade in the whole backlog, budget a full fresh pass once the itemized list above is cleared.

---

## 6. Grade 6 — only ~27% ever checked

**Already fixed (2 total, days not preserved — spot-check).**

**Confirmed bad — needs fix:**
- [ ] Day 1, SocialStudies ("Canada's Place in the World") — got Day 2's video by mistake (Day 2's own lesson uses it correctly — do NOT touch Day 2)
- [ ] Day 30 (all 4 subjects) — no videoUrl at all
- [ ] 3 more "irrelevant" per the eod summary, days not itemized

**Low priority (likely non-issues under the current too-long-is-fine quality rule, verify relevance only, don't replace purely for length):**
- [ ] 4 "too-long" flags (21-42 min) — per the standing quality rule, length alone is not disqualifying; only replace if also off-topic

**Ambiguous — needs judgment call:**
- [ ] Day 5, Language (labeled "Grades 3-5," not 6 specifically — judge whether content is still grade-appropriate)
- [ ] Day 6, SocialStudies (covers only half the lesson's comparison topic)
- [ ] 8 more ambiguous flags per the eod summary, days not itemized

**Unchecked/unverified:** Days 7-29 almost entirely (the original agent's bash tools were down for its whole run) — largest unverified gap in the backlog after Grade 5.

---

## 7. Grade 8 — ~64% checked, 0 fixes ever applied

**Confirmed bad — needs fix (30 total: 4 missing + 26 irrelevant/wrong-length):**
- [ ] Day 30 (all 4 subjects) — no videoUrl at all
- [ ] `QbTm6m7198g` ("Do This Before Your History Exam," 28 seconds — also too-short, a real defect) reused across 4 History lessons: Days 24, 27, 28, 29 — fix all 4 individually
- [ ] 13 confirmed-bad from the original pass (Indian board-exam content, wrong-country history videos, clickbait Shorts, wrong grade level) spanning Days 2, 5, 6, 10, 11, 20, 24 (x2), 25, 26 (x2), 27, 29
- [ ] `zz440EuFK8Q` also reused across 5 different day/topic combos in Grade 8's History slot per the original report — check this first alongside the QbTm6m7198g cluster, likely overlaps with some of the 13 above

**Ambiguous — needs judgment call (10 total):**
- [ ] Days 8, 9, 12 (x2), 13, 14, 18, 19 (x2), 26

**Unchecked/unverified:** ~39 of 107 videos, spread across many days.

---

## 8. Grade 7 — re-verification pass (previously marked "complete", proven unreliable)

**Confirmed fixed 2026-08-20 (this session, do not re-check):**
- [x] Day 5, SocialStudies ("Review: Early Canada and Geography") — was a single mismatched "Introducing the Regions of Canada" video on a 4-topic review lesson (New France/Seven Years War, Rebellions of 1837-38, climate zones, natural resources) → replaced with a proper 3-video combo per the Multi-video policy (New France/Seven Years War, Rebellions of 1837-38, Climate Zones)

**From the original (pre-"complete") July 21 partial pass — verify these are still actually fixed, since the later "complete" claim turned out not to be fully trustworthy:**
- [ ] Day 2, SocialStudies — was flagged as a Confederation video used for an 1800-1850 conflict lesson (mixed up with Day 6). Check current state.
- [ ] Day 14, SocialStudies — was flagged as a Seven Years' War video used for a WWI lesson (mixed up with Day 1). Check current state.
- [ ] Day 3, Language — was flagged as covering only "tone," not "theme" (ambiguous). Check current state.
- [ ] Day 29, SocialStudies and all of Day 30 — were flagged as having no videoUrl at all. Check current state (may have been filled by the "complete" 2026-07-22 pass, or may still be genuinely missing).

**Everything else (Days 1, 4-13, 15-28, all subjects not listed above):** never itemized as bad in either report, and the eod file claims a full audit completed 2026-07-22 with all 12 found issues fixed. Given the Day 5 slip-through, do a light spot-check (pull title/description via free oembed/snippet call for a sample of ~10-15 blocks not already covered above, compare to lesson content) before fully trusting this grade is clean. If the spot-check turns up more misses, escalate to a full re-check of the grade like the others above.

---

## 9. Grades 0-4 — lowest priority, spot-check only

Previously audited AND fixed (not just classified) on 2026-07-21/22:
- Grade 0: 15 fixes (first-ever full audit for this grade)
- Grade 1: 17 fixes (first-ever full audit)
- Grade 2: 13 fixes (length/missing pass; topic-relevance already audited earlier)
- Grade 3: 7 fixes (length/missing pass; topic-relevance already audited earlier)
- Grade 4: 2 fixes (length pass, partial) — 9 more "too-long" (42min-2hr) videos flagged on Days 24/27/28/30 review lessons, several sharing reused video IDs across multiple days, but per the standing too-long-is-fine quality rule these are likely NOT real defects unless also off-topic. Spot-check relevance, don't replace purely for length.

**Action:** once Grades 5-9 above are cleared, do a light spot-check pass here (a handful of blocks per grade via the free oembed/snippet check) rather than a full re-audit, given these were the most thoroughly worked grades in July and (unlike Grade 7) were never given a blanket "100% complete, trust it" claim that later proved wrong.
