// Central allow-list for admin-only areas (currently just the feedback
// inbox at /admin/feedback). Defaults to Khurram's account so the feature
// works with zero configuration; set ADMIN_EMAILS (comma-separated) to
// add more admins later.
//
// Note: process.env.ADMIN_EMAILS is only ever populated server-side (no
// NEXT_PUBLIC_ prefix), so a client component calling isAdminEmail() will
// always see just the default list. That's fine -- the client-side check
// is only used to gate the UI for a nicer experience; the real
// enforcement happens server-side in the API routes, where the env var
// (if set) is available.
const DEFAULT_ADMIN_EMAILS = ['khurram.athar@gmail.com'];

export function getAdminEmails(): string[] {
  const raw = process.env.ADMIN_EMAILS;
  if (!raw) return DEFAULT_ADMIN_EMAILS;
  const parsed = raw.split(',').map((e) => e.trim().toLowerCase()).filter(Boolean);
  return parsed.length > 0 ? parsed : DEFAULT_ADMIN_EMAILS;
}

export function isAdminEmail(email?: string | null): boolean {
  if (!email) return false;
  return getAdminEmails().includes(email.toLowerCase());
}
