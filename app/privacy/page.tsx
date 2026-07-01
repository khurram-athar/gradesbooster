import Link from 'next/link';
import Image from 'next/image';
import { Button } from '@/components/ui/button';

export const metadata = {
  title: 'Privacy Policy — GradesBooster',
  description: 'How GradesBooster collects, uses, and protects your information.',
};

export default function PrivacyPage() {
  return (
    <div className="min-h-screen bg-background">
      {/* Nav */}
      <header className="sticky top-0 z-50 border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="mx-auto max-w-4xl px-4 h-14 flex items-center justify-between">
          <Link href="/" className="flex items-center">
            <Image src="/logo.svg" alt="GradesBooster" width={160} height={38} priority />
          </Link>
          <Button asChild variant="ghost" size="sm">
            <Link href="/auth">Sign In</Link>
          </Button>
        </div>
      </header>

      <main className="mx-auto max-w-4xl px-4 py-16">
        <h1 className="text-4xl font-bold text-foreground mb-2">Privacy Policy</h1>
        <p className="text-sm text-muted-foreground mb-10">Last updated: July 1, 2026</p>

        <div className="prose prose-sm max-w-none space-y-8 text-foreground">

          <section>
            <h2 className="text-xl font-semibold mb-3">1. Who We Are</h2>
            <p className="text-muted-foreground leading-relaxed">
              GradesBooster ("we", "our", or "us") is an Ontario-based educational platform at{' '}
              <a href="https://gradesbooster.ai" className="text-primary hover:underline">gradesbooster.ai</a>{' '}
              that provides curriculum-aligned daily learning plans for K–12 students. We are
              committed to protecting the privacy of parents and the children in their care.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">2. What Information We Collect</h2>
            <p className="text-muted-foreground leading-relaxed mb-3">
              We collect only what is necessary to provide the service:
            </p>
            <ul className="list-disc list-inside space-y-2 text-muted-foreground">
              <li><strong className="text-foreground">Parent account:</strong> email address and display name, provided when you register.</li>
              <li><strong className="text-foreground">Child profiles:</strong> first name and grade level, entered by the parent. We do not collect dates of birth, addresses, or any other identifying information about children.</li>
              <li><strong className="text-foreground">Learning progress:</strong> quiz scores and lesson completion status, stored per child under the parent's account.</li>
              <li><strong className="text-foreground">Usage data:</strong> standard server logs (IP address, browser type, pages visited) retained for up to 30 days for security and performance purposes.</li>
            </ul>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">3. Children's Privacy (COPPA &amp; PIPEDA)</h2>
            <p className="text-muted-foreground leading-relaxed">
              GradesBooster does not allow children to create accounts. All accounts are held by
              parents or guardians (18+). Child profiles exist solely within the parent's account and
              contain only a first name and grade. We do not knowingly collect personal information
              directly from children under 13. If you believe a child has provided us with personal
              information without parental consent, please contact us and we will delete it promptly.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">4. How We Use Your Information</h2>
            <ul className="list-disc list-inside space-y-2 text-muted-foreground">
              <li>To authenticate your account and keep your data secure.</li>
              <li>To display learning progress and quiz results to you on the dashboard.</li>
              <li>To improve the platform and fix bugs (via aggregated, anonymous usage data).</li>
              <li>To send essential service emails (e.g., password reset). We do not send marketing emails.</li>
            </ul>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">5. Data Storage &amp; Security</h2>
            <p className="text-muted-foreground leading-relaxed">
              Your data is stored in Google Firebase (Firestore), hosted in North American data
              centres. Firebase enforces server-side security rules so that each parent can only
              access their own account and child data. All data is transmitted over HTTPS. We do not
              sell, rent, or share your personal information with third parties for advertising or
              marketing purposes.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">6. Third-Party Services</h2>
            <p className="text-muted-foreground leading-relaxed mb-3">
              GradesBooster uses the following third-party services:
            </p>
            <ul className="list-disc list-inside space-y-2 text-muted-foreground">
              <li><strong className="text-foreground">Google Firebase</strong> — authentication and database. Subject to <a href="https://firebase.google.com/support/privacy" target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">Firebase Privacy Policy</a>.</li>
              <li><strong className="text-foreground">Vercel</strong> — web hosting and CDN. Subject to <a href="https://vercel.com/legal/privacy-policy" target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">Vercel Privacy Policy</a>.</li>
              <li><strong className="text-foreground">YouTube</strong> — some lessons embed YouTube videos. YouTube may set cookies when a video is played. Subject to <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">Google Privacy Policy</a>.</li>
            </ul>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">7. Your Rights</h2>
            <p className="text-muted-foreground leading-relaxed">
              Under Canada's PIPEDA, you have the right to access the personal information we hold
              about you, correct inaccuracies, or request deletion of your account and all associated
              data. To exercise any of these rights, email us at{' '}
              <a href="mailto:privacy@gradesbooster.ai" className="text-primary hover:underline">
                privacy@gradesbooster.ai
              </a>
              . We will respond within 30 days.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">8. Cookies</h2>
            <p className="text-muted-foreground leading-relaxed">
              We use only essential cookies required for authentication (Firebase session tokens).
              We do not use advertising cookies or tracking pixels.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">9. Changes to This Policy</h2>
            <p className="text-muted-foreground leading-relaxed">
              We may update this policy from time to time. When we do, we will update the "Last
              updated" date at the top of this page. Continued use of GradesBooster after changes
              are posted constitutes acceptance of the updated policy.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold mb-3">10. Contact Us</h2>
            <p className="text-muted-foreground leading-relaxed">
              Questions or concerns about this policy?{' '}
              <a href="mailto:privacy@gradesbooster.ai" className="text-primary hover:underline">
                privacy@gradesbooster.ai
              </a>
            </p>
          </section>

        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-border mt-16">
        <div className="mx-auto max-w-4xl px-4 py-8 flex flex-col md:flex-row items-center justify-between gap-4 text-sm text-muted-foreground">
          <span>© {new Date().getFullYear()} GradesBooster. Ontario, Canada.</span>
          <div className="flex gap-6">
            <Link href="/#faq" className="hover:text-foreground transition-colors">FAQ</Link>
            <Link href="/auth" className="hover:text-foreground transition-colors">Sign In</Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
