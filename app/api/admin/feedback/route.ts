import { NextRequest, NextResponse } from 'next/server';
import { adminAuth, adminDb } from '@/lib/firebase-admin';
import { isAdminEmail } from '@/lib/admin';

// GET /api/admin/feedback
// Admin-only read of the `feedback` collection. The collection denies all
// client reads (see firestore.rules), so this route uses the Admin SDK
// (which bypasses security rules) after verifying the caller's Firebase
// ID token belongs to an allow-listed admin email (see lib/admin.ts).

export async function GET(req: NextRequest) {
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

    if (!isAdminEmail(decoded.email)) {
      return NextResponse.json({ error: 'Not authorized.' }, { status: 403 });
    }

    const snapshot = await adminDb
      .collection('feedback')
      .orderBy('createdAt', 'desc')
      .limit(300)
      .get();

    const feedback = snapshot.docs.map((doc) => {
      const data = doc.data();
      const createdAt: FirebaseFirestore.Timestamp | undefined = data.createdAt;
      return {
        id: doc.id,
        uid: (data.uid as string) ?? null,
        email: (data.email as string) ?? null,
        message: (data.message as string) ?? '',
        category: (data.category as string) ?? 'other',
        page: (data.page as string) ?? null,
        createdAt: createdAt ? createdAt.toDate().toISOString() : null,
      };
    });

    return NextResponse.json({ feedback });
  } catch (err) {
    console.error('[/api/admin/feedback]', err);
    return NextResponse.json({ error: 'Something went wrong.' }, { status: 500 });
  }
}
