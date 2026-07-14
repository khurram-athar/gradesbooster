<!-- BEGIN:live-site-architecture -->
# READ THIS FIRST: what's actually live

**Confirmed 2026-07-14, via direct inspection of both repos plus Lovable's own confirmation:** the live, deployed site is `gradesbooster-lovable` (TanStack Start v1 + React 19 + Tailwind v4 + Supabase, on Cloudflare Workers) — **not** this repo (`gradesbooster`, Next.js 16 + Firebase). The migration described further down in this file is complete. This repo's app code (`app/`, `components/`, `lib/firestore.ts`, `lib/firebase*.ts`, API routes, etc.) is legacy and does **not** serve production traffic, regardless of how current or complete it looks.

**What still matters in this repo:** only `data/gradeN.ts` / `data/gradeN.json` (curriculum content) and the `gen_*.py` / `build_json.py` scripts that produce them. Everything else here is dead code from the pre-migration app — don't extend it expecting it to go live.

**How curriculum data actually reaches the live site (confirmed 2026-07-14):**
1. Edit `data/gradeN.ts`, run `python3 build_json.py --grade N` to regenerate the matching `.json`, commit both (plus the generator script), and `git push` to `main` on `github.com/khurram-athar/gradesbooster`.
2. `gradesbooster-lovable/src/lib/curriculum-sync.server.ts` reads `https://raw.githubusercontent.com/khurram-athar/gradesbooster/main/data/grade{N}.json` directly off GitHub — so nothing downstream sees an edit until it's actually pushed to `main`, not just committed locally.
3. **The sync is on-demand, not automatic or scheduled.** Pushing to GitHub does not update the live site by itself. After any curriculum push, tell Khurram he (or whoever's signed in as admin) needs to visit `/parent/curriculum` on the live site and click "Sync now" per grade (or all grades) — that's the step that actually pulls the new JSON into Supabase. Don't assume this happens automatically, and don't forget to mention it.

**For anything that isn't curriculum data** — features, UI, auth, admin pages, email, backend logic, anything that would live under `app/` in a Next.js mental model — that work belongs in `gradesbooster-lovable`, not here. In practice, the right move is to draft a clear, self-contained prompt describing the desired change and have Khurram relay it to Lovable, rather than writing the code directly in either repo. Lovable knows the live app's actual current schema, routes, and conventions, which can drift from anything documented in this file. **Do not port Next.js/Firebase-shaped code into this repo (or write TanStack/Supabase code here) expecting it to reach production.**

This exact mistake happened on 2026-07-14: an admin feedback feature (page + API routes + email notification) was built directly in this repo's Next.js/Firebase code, on the assumption it was the live app. Lovable caught the mismatch before anything deployed — the live app already had its own feedback flow into Supabase (`feedback_submissions` table, `has_role('admin')` gating, an existing `feedback-digest.server.ts` cron) with a completely different shape. No harm done since it never shipped, but going forward: when a request involves anything beyond `data/gradeN.ts`/`.json`, assume `gradesbooster-lovable` is the live app unless told otherwise, and check with Lovable (via a drafted prompt) before writing non-curriculum application code in this repo.
<!-- END:live-site-architecture -->

<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

<!-- BEGIN:lovable-migration-target -->
# Target stack (historical context — migration is now COMPLETE, see "READ THIS FIRST" above)

As of 2026-07-03, this repo was still Next.js 16 + Firebase, and Khurram was using Lovable AI in parallel to migrate/redesign the site toward a different target stack in a separate repo (`gradesbooster-lovable`). That migration finished sometime before 2026-07-14 — the live site now runs entirely from `gradesbooster-lovable`. This repo continues to exist solely as the source of truth for curriculum data (see above); Lovable does not build the live app's UI/backend here anymore. The stack notes below describe `gradesbooster-lovable`, kept here for reference since this file was originally written before the two repos' roles were this clearly separated.

**Required git workflow around curriculum work (per Lovable's instructions, 2026-07-04):**
1. Before starting any curriculum work: `git pull` first, so Claude has Lovable's latest landing page code as the base.
2. After finishing and committing curriculum changes: `git push`, so Lovable's next pull picks up the curriculum files.

Important limitation: this sandbox cannot reach github.com (confirmed repeatedly — `git pull`/`git push` fail with a 403 from the proxy). Claude should still attempt `git pull` at the start of a curriculum session and `git push` at the end as the first and last steps, but when these fail, Claude must tell Khurram plainly that he needs to run `git pull` before handing Claude curriculum work, and `git push` after Claude finishes, from his own local Terminal.

Target stack guidelines from Lovable (apply to any *new* app code — routing, auth, components, backend — not to curriculum data):
- Stack: TanStack Start v1 + React 19 + Tailwind CSS v4 + Supabase (Lovable Cloud backend).
- Design: Modern, friendly edtech landing page. Primary monogram logo "Gb" (gradient, locked across all pages). Ontario K–12 pilot; use "K–12" copy and present kindergarten as "Kindergarten" (not split).
- Auth: Google sign-in only; avoid password flows. Parent-only area unlocks via Google, not password.
- Logo component: use shared `BrandLogo` component in `src/components/brand-logo.tsx` on all pages — do not recreate inline logo SVGs.
- Mobile: all pages must be fully mobile-friendly; test with mobile viewport before finishing.
- Routes: file-based routing under `src/routes/`. Keep metadata unique per route (title, description, og tags). Add `og:image` only at leaf routes with a real image URL.
- Backend: use `createServerFn` for app-internal logic; public APIs/webhooks under `/api/public/*`. Enable RLS + GRANTs on every new Supabase table. User roles live in a separate `user_roles` table, never on `profiles`.
- Memory: project memory referenced as `mem://index.md` (Lovable-internal — not directly readable by Claude; if this becomes a real file in the repo, read it before edits).

Curriculum content (`data/gradeN.ts`) stays as plain, framework-agnostic TypeScript data files regardless of this migration — confirmed with Khurram on 2026-07-03. Keep editing those directly; no need to route curriculum work through Supabase unless he says otherwise.
<!-- END:lovable-migration-target -->

<!-- BEGIN:visual-design-lock -->
# Visual design consistency (locked 2026-07-07, per Khurram)

Every future iteration — by Claude or Lovable — must preserve or improve on the current look and feel. Buttons, color scheme, imagery, and charts/graphs should never regress or get casually swapped out for something different; only intentional, explicitly-requested redesigns should change them.

Current design system (read from `gradesbooster-lovable/src/styles.css` and components, 2026-07-07):
- **Brand colors:** primary blue `--brand` #2563eb / `--brand-dark` #1e40af, success green #10b981, warm amber accent, plum accent, friendly coral accent, ink text, warm-cream/soft-bg backgrounds. All defined as CSS custom properties in `src/styles.css` — reuse these tokens for any new UI, don't hardcode new colors.
- **Font:** Plus Jakarta Sans (`--font-jakarta`) throughout.
- **Corner radius:** 1rem base (`--radius`), rounded-2xl/3xl look site-wide.
- **Logo:** shared `BrandLogo` component (`src/components/brand-logo.tsx`) — reuse on every page, never recreate inline.
- **Buttons:** shadcn `Button` component (`src/components/ui/button.tsx`) with existing variants (default, destructive, outline, secondary, ghost, link) and sizes (default, sm, lg, icon) — use these variants for new buttons rather than one-off styles.
- **Charts/graphs:** shared chart color tokens `--chart-1` through `--chart-5` (`src/components/ui/chart.tsx`) — any new graph/data visualization should pull from these, not introduce a new palette.

When proposing a visual change (new page, new component, redesign of an existing one), treat it as additive — same tokens, same components, better content/imagery — unless Khurram explicitly asks for a redesign. If a Lovable prompt risks touching visual style, add an explicit line telling it not to change colors, buttons, the logo, or existing charts.
<!-- END:visual-design-lock -->
