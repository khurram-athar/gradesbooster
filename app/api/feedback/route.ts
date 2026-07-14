import { NextRequest, NextResponse } from 'next/server';
import { Resend } from 'resend';
import { adminAuth, adminDb } from '@/lib/firebase-admin';
import { FieldValue } from 'firebase-admin/firestore';
import { getAdminEmails } from '@/lib/admin';

// POST /api/feedback
// Replaces the old client-side direct write to the `feedback` Firestore
// collection (that collection denies client reads entirely -- see
// firestore.rules -- so it could only ever be reviewed via the Firebase
// Console). Writing it here instead, via the Admin SDK, lets us also fire
// off a best-effort email notification the moment feedback comes in, and
// keeps the write path server-verified (checks the caller's Firebase ID
// token rather than trusting a client-supplied uid).

const CATEGORIES = new Set(['bug', 'content', 'idea', 'other']);
const MAX_MESSAGE_LENGTH = 4000;

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function buildFeedbackEmailHtml(opts: {
  message: string;
  category: string;
  email: string;
  page: string | null;
}): string {
  const { message, category, email, page } = opts;
  return `
    <div style="max-width:480px;margin:0 auto;font-family:sans-serif;">
      <h2 style="color:#111;margin:0 0 12px;">New GradesBooster feedback</h2>
      <p style="margin:4px 0;color:#333;"><strong>Category:</strong> ${escapeHtml(category)}</p>
      <p style="margin:4px 0;color:#333;"><strong>From:</strong> ${escapeHtml(email)}</p>
      ${page ? `<p style="margin:4px 0;color:#333;"><strong>Page:</strong> ${escapeHtml(page)}</p>` : ''}
      <div style="margin-top:16px;padding:16px;background:#f8fafc;border-radius:12px;white-space:pre-wrap;line-height:1.5;color:#111;">${escapeHtml(message)}</div>
      <p style="margin-top:20px;font-size:13px;color:#999;">
        View all feedback any time at
        <a href="https://gradesbooster.ai/admin/feedback" style="color:#2563eb;">gradesbooster.ai/admin/feedback</a>.
      </p>
    </div>
  `;
}

export async function POST(req: NextRequest) {
  try {
    const authHeader = req.headers.get('authorization') || '';
    const token = authHeader.startsWith('Bearer ') ? authHeader.slice(7) : '';
    if (!token) {
      return NextResponse.json({ error: 'Not signed in.' }, { status: 401 });
    }

    let decoded;
    try {
      decoded = await adminAuth.verifyIdToken(token);
    } catch {
      return NextResponse.json({ error: 'Invalid session. Please sign in again.' }, { status: 401 });
    }

    const body = await req.json().catch(() => null);
    const message = typeof body?.message === 'string' ? body.message.trim() : '';
    const category =
      typeof body?.category === 'string' && CATEGORIES.has(body.category) ? body.category : 'other';
    const page = typeof body?.page === 'string' ? body.page.slice(0, 200) : null;

    if (!message) {
      return NextResponse.json({ error: 'Message is required.' }, { status: 400 });
    }
    if (message.length > MAX_MESSAGE_LENGTH) {
      return NextResponse.json({ error: 'Message is too long.' }, { status: 400 });
    }

    const ref = adminDb.collection('feedback').doc();
    await ref.set({
      uid: decoded.uid,
      email: decoded.email ?? null,
      message,
      category,
      page,
      createdAt: FieldValue.serverTimestamp(),
    });

    // Best-effort email notification -- never let a failure here fail the
    // feedback submission itself.
    if (process.env.RESEND_API_KEY) {
      try {
        const resend = new Resend(process.env.RESEND_API_KEY);
        await resend.emails.send({
          from: 'GradesBooster <feedback@gradesbooster.ai>',
          to: getAdminEmails(),
          subject: `New feedback (${category}): ${message.slice(0, 60)}${message.length > 60 ? '…' : ''}`,
          html: buildFeedbackEmailHtml({
            message,
            category,
            email: decoded.email ?? 'unknown',
            page,
          }),
        });
      } catch (err) {
        console.error('[/api/feedback] failed to send notification email', err);
      }
    }

    return NextResponse.json({ ok: true, id: ref.id });
  } catch (err) {
    console.error('[/api/feedback]', err);
    return NextResponse.json({ error: 'Something went wrong.' }, { status: 500 });
  }
}
