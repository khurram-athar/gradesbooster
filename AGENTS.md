<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

<!-- BEGIN:lovable-migration-target -->
# Future stack (Lovable AI is migrating this repo — same repo, main branch)

As of 2026-07-03, this repo is still Next.js 16 + Firebase. Khurram is using Lovable AI in parallel to migrate/redesign the site toward a different target stack. Both Lovable and Claude commit to the same repo/branch, so **pull before starting work and push promptly after committing** to avoid working from a stale base.

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
