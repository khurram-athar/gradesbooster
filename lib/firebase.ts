import { initializeApp, getApps, getApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { initializeAppCheck, ReCaptchaV3Provider } from 'firebase/app-check';

const firebaseConfig = {
  apiKey: 'AIzaSyCoS1Q5GDSdLE4IAI-1AOExa3HJaMBPLzY',
  authDomain: 'summer-review-2026.firebaseapp.com',
  projectId: 'summer-review-2026',
  storageBucket: 'summer-review-2026.firebasestorage.app',
  messagingSenderId: '259878643151',
  appId: '1:259878643151:web:8b4c94bac012e83f3f1eba',
};

const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApp();

// App Check (reCAPTCHA v3) — protects Firebase from abuse.
// Set NEXT_PUBLIC_RECAPTCHA_SITE_KEY in your Vercel environment variables.
// In development, enable the debug token:
//   (self as any).FIREBASE_APPCHECK_DEBUG_TOKEN = true;
if (typeof window !== 'undefined' && process.env.NEXT_PUBLIC_RECAPTCHA_SITE_KEY) {
  initializeAppCheck(app, {
    provider: new ReCaptchaV3Provider(process.env.NEXT_PUBLIC_RECAPTCHA_SITE_KEY),
    isTokenAutoRefreshEnabled: true,
  });
}

export const auth = getAuth(app);
export const db = getFirestore(app);
export default app;
