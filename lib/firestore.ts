'use client';

import {
  collection,
  doc,
  getDocs,
  setDoc,
  deleteDoc,
  getDoc,
  serverTimestamp,
  query,
  orderBy,
} from 'firebase/firestore';
import { db } from './firebase';
import type { KidProfile, QuizResult } from '@/types';

// ── Kid profiles ─────────────────────────────────────────────

export async function loadKids(uid: string): Promise<KidProfile[]> {
  const ref = collection(db, 'users', uid, 'kids');
  const snap = await getDocs(query(ref, orderBy('createdAt')));
  return snap.docs.map((d) => ({ id: d.id, ...d.data() } as KidProfile));
}

export async function saveKid(
  uid: string,
  data: Omit<KidProfile, 'id' | 'createdAt'>,
  kidId?: string | null,
): Promise<string> {
  const ref = kidId
    ? doc(db, 'users', uid, 'kids', kidId)
    : doc(collection(db, 'users', uid, 'kids'));

  const existing = kidId ? (await getDoc(ref)).data() : null;

  await setDoc(
    ref,
    {
      ...data,
      createdAt: existing?.createdAt ?? Date.now(),
      updatedAt: serverTimestamp(),
    },
    { merge: true },
  );

  return ref.id;
}

export async function deleteKid(uid: string, kidId: string): Promise<void> {
  // Delete all results first
  const resultsRef = collection(db, 'users', uid, 'kids', kidId, 'results');
  const resultsSnap = await getDocs(resultsRef);
  await Promise.all(resultsSnap.docs.map((d) => deleteDoc(d.ref)));
  // Then delete the kid doc
  await deleteDoc(doc(db, 'users', uid, 'kids', kidId));
}

// ── Quiz results ──────────────────────────────────────────────

function resultId(grade: number, day: number, subject: string) {
  return `g${grade}_d${day}_${subject}`;
}

export async function loadKidResults(
  uid: string,
  kidId: string,
  grade: number,
): Promise<Map<string, QuizResult>> {
  const ref = collection(db, 'users', uid, 'kids', kidId, 'results');
  const snap = await getDocs(ref);
  const map = new Map<string, QuizResult>();
  snap.docs.forEach((d) => map.set(d.id, d.data() as QuizResult));
  return map;
}

export async function saveResult(
  uid: string,
  kidId: string,
  grade: number,
  day: number,
  dayLabel: string,
  subject: string,
  score: number,
  total: number,
): Promise<void> {
  const id = resultId(grade, day, subject);
  const ref = doc(db, 'users', uid, 'kids', kidId, 'results', id);
  await setDoc(ref, {
    grade: String(grade),
    day,
    dayLabel,
    subject,
    score,
    total,
    date: new Date().toISOString().slice(0, 10),
    updatedAt: Date.now(),
  });
}

// ── Feedback ──────────────────────────────────────────────────

export async function submitFeedback(
  uid: string,
  email: string | null,
  message: string,
  category: string,
): Promise<void> {
  const ref = doc(collection(db, 'feedback'));
  await setDoc(ref, {
    uid,
    email: email ?? null,
    message,
    category,
    page: typeof window !== 'undefined' ? window.location.pathname : null,
    createdAt: serverTimestamp(),
  });
}

export async function loadAllKidResults(
  uid: string,
  kids: KidProfile[],
): Promise<Map<string, Map<string, QuizResult>>> {
  // Returns: kidId -> resultId -> QuizResult
  const entries = await Promise.all(
    kids.map(async (kid) => {
      const results = await loadKidResults(uid, kid.id, kid.grade);
      return [kid.id, results] as [string, Map<string, QuizResult>];
    }),
  );
  return new Map(entries);
}
