import { initializeApp, getApps, getApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: 'AIzaSyCoS1Q5GDSdLE4IAI-1AOExa3HJaMBPLzY',
  authDomain: 'summer-review-2026.firebaseapp.com',
  projectId: 'summer-review-2026',
  storageBucket: 'summer-review-2026.firebasestorage.app',
  messagingSenderId: '259878643151',
  appId: '1:259878643151:web:8b4c94bac012e83f3f1eba',
};

const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApp();

export const auth = getAuth(app);
export const db = getFirestore(app);
export default app;
