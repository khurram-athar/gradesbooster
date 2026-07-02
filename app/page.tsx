'use client';

import Link from 'next/link';
import Image from 'next/image';
import { useState } from 'react';
import { useAuth } from '@/components/auth-provider';
import { Button } from '@/components/ui/button';
import {
  GraduationCap,
  BookOpen,
  BarChart2,
  Users,
  Clock,
  ChevronDown,
  CheckCircle,
  Star,
  Sparkles,
  Globe,
  Lock,
} from 'lucide-react';

// ── FAQ accordion ────────────────────────────────────────────────────────────

const FAQS = [
  {
    q: 'Is GradesBooster free to use?',
    a: 'Yes — completely free for parents. Create an account, add your children, and start learning right away with no credit card required.',
  },
  {
    q: 'Which curriculum does it follow?',
    a: 'Currently aligned to the Ontario K–12 curriculum. Support for other Canadian provinces and US states is on the way.',
  },
  {
    q: 'How does each lesson work?',
    a: 'Each subject lesson has two parts: first, your child watches a short curated YouTube video on that day\'s topic, then completes a 5-question multiple-choice quiz. The video and quiz together take about 10–15 minutes per subject.',
  },
  {
    q: 'How much time does it take each day?',
    a: 'Typically 30–60 minutes per day covering 4 subjects. Each subject has a short video plus a 5-question quiz, so the pace is relaxed and focused.',
  },
  {
    q: 'Which grades have content right now?',
    a: 'All grades — Kindergarten through Grade 12 — are fully available with 30 days of content each. Every grade has been written and aligned to Ontario curriculum expectations.',
  },
  {
    q: 'Do my kids need their own accounts?',
    a: 'No. Kids access their lessons through your parent account — no passwords or emails needed for children. Simply select your child\'s name and hand them the device.',
  },
  {
    q: 'Can I track my child\'s progress?',
    a: 'Yes. The Parent Dashboard shows quiz scores, completion rates, and a full history for every child. You can also export results to a CSV file.',
  },
  {
    q: 'Does it work on phones and tablets?',
    a: 'Absolutely. GradesBooster is fully responsive and works great on any device — phone, tablet, or computer.',
  },
  {
    q: 'What subjects are covered?',
    a: 'Elementary grades cover Language Arts, Mathematics, Science, and Social Studies. High school grades include subject-specific courses like Physics, Chemistry, Biology, History, and Geography.',
  },
  {
    q: 'What if a video doesn\'t load?',
    a: 'Each video is matched to the day\'s topic using YouTube search. If a video doesn\'t load, a "Search YouTube" link appears below it so your child can find an alternative video on the same topic instantly.',
  },
];

function FAQItem({ q, a }: { q: string; a: string }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="border-b border-border last:border-0">
      <button
        className="w-full flex items-center justify-between gap-4 py-5 text-left"
        onClick={() => setOpen((v) => !v)}
      >
        <span className="font-semibold text-foreground">{q}</span>
        <ChevronDown
          className={`h-5 w-5 shrink-0 text-muted-foreground transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
        />
      </button>
      {open && (
        <p className="pb-5 text-muted-foreground leading-relaxed -mt-1">{a}</p>
      )}
    </div>
  );
}

// ── Grade grid ────────────────────────────────────────────────────────────────

const GRADE_GROUPS = [
  { label: 'Kindergarten', grades: ['K'], ready: [true] },
  { label: 'Primary', grades: ['1', '2', '3'], ready: [true, true, true] },
  { label: 'Junior', grades: ['4', '5', '6'], ready: [true, true, true] },
  { label: 'Intermediate', grades: ['7', '8'], ready: [true, true] },
  { label: 'High School', grades: ['9', '10', '11', '12'], ready: [true, true, true, true] },
];

// ── Landing page ─────────────────────────────────────────────────────────────

export default function LandingPage() {
  const { user, loading } = useAuth();

  return (
    <div className="flex flex-col min-h-screen">

      {/* ── Top nav ── */}
      <header className="sticky top-0 z-50 border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="mx-auto max-w-6xl px-4 h-14 flex items-center justify-between">
          <Link href="/" className="flex items-center">
            <Image src="/logo.svg" alt="GradesBooster" width={160} height={38} priority />
          </Link>
          <div className="flex items-center gap-2">
            {!loading && (
              user ? (
                <>
                  <Button asChild variant="outline" className="gap-1.5">
                    <Link href="/dashboard">
                      <Lock className="h-3.5 w-3.5" />
                      <span className="hidden sm:inline">Parent Dashboard</span>
                      <span className="sm:hidden">Dashboard</span>
                    </Link>
                  </Button>
                  <Button asChild>
                    <Link href="/home">On to Today&apos;s Lesson →</Link>
                  </Button>
                </>
              ) : (
                <>
                  <Button asChild variant="ghost">
                    <Link href="/auth">Sign In</Link>
                  </Button>
                  <Button asChild>
                    <Link href="/auth">Get Started Free</Link>
                  </Button>
                </>
              )
            )}
          </div>
        </div>
      </header>

      <main className="flex-1">

        {/* ── Hero ── */}
        <section className="relative overflow-hidden bg-gradient-to-br from-teal-600 via-emerald-600 to-green-700 text-white">
          {/* Decorative circles */}
          <div className="absolute top-0 right-0 w-96 h-96 bg-white/5 rounded-full -translate-y-1/2 translate-x-1/3 blur-3xl" />
          <div className="absolute bottom-0 left-0 w-72 h-72 bg-white/5 rounded-full translate-y-1/2 -translate-x-1/4 blur-3xl" />

          <div className="relative mx-auto max-w-5xl px-4 py-24 md:py-32 text-center">
            <div className="inline-flex items-center gap-2 bg-white/15 backdrop-blur rounded-full px-4 py-1.5 text-sm font-medium mb-6">
              <Sparkles className="h-4 w-4" />
              Ontario K–12 Curriculum · Completely Free
            </div>

            <h1 className="text-4xl md:text-6xl font-extrabold leading-tight tracking-tight mb-6">
              Boost Your Child&apos;s<br />
              <span className="text-yellow-300">Academic Confidence</span>
            </h1>

            <p className="text-lg md:text-xl text-white/80 max-w-2xl mx-auto mb-10 leading-relaxed">
              Daily curriculum-aligned lessons for students in grades K–12.
              30 minutes a day builds the habits that transform report cards.
            </p>

            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Button
                asChild
                size="lg"
                className="bg-white text-teal-700 hover:bg-white/90 font-bold text-base px-8"
              >
                <Link href="/auth">Get Started Free →</Link>
              </Button>
              <Button
                asChild
                size="lg"
                variant="outline"
                className="border-white/40 text-white bg-white/10 hover:bg-white/20 text-base px-8"
              >
                <a href="#how-it-works">See How It Works</a>
              </Button>
            </div>
          </div>
        </section>

        {/* ── Stats bar ── */}
        <section className="border-b border-border bg-card">
          <div className="mx-auto max-w-5xl px-4 py-6 grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            {[
              { value: 'K–12', label: 'All Grades' },
              { value: '4+', label: 'Subjects per Day' },
              { value: '30 days', label: 'Per Learning Plan' },
              { value: '100% Free', label: 'Always' },
            ].map(({ value, label }) => (
              <div key={label}>
                <p className="text-2xl md:text-3xl font-extrabold text-primary">{value}</p>
                <p className="text-sm text-muted-foreground mt-0.5">{label}</p>
              </div>
            ))}
          </div>
        </section>

        {/* ── Features ── */}
        <section className="mx-auto max-w-5xl px-4 py-20">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold mb-3">Everything your child needs to succeed</h2>
            <p className="text-muted-foreground text-lg max-w-xl mx-auto">
              Built by educators, designed for real families.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            {[
              {
                icon: BookOpen,
                color: 'bg-purple-100 text-purple-700',
                title: 'Curriculum-Aligned',
                desc: 'Every lesson maps directly to Ontario curriculum expectations — the same content covered at school.',
              },
              {
                icon: BarChart2,
                color: 'bg-blue-100 text-blue-700',
                title: 'Progress Tracking',
                desc: 'Parents see quiz scores and completion rates for every child, every day, in the dashboard.',
              },
              {
                icon: Users,
                color: 'bg-green-100 text-green-700',
                title: 'Multiple Children',
                desc: 'Add unlimited kids under one parent account. Each child\'s progress is tracked separately.',
              },
              {
                icon: Clock,
                color: 'bg-orange-100 text-orange-700',
                title: '30 Min/Day',
                desc: 'Short, focused sessions that fit into any family\'s schedule — summer or year-round.',
              },
            ].map(({ icon: Icon, color, title, desc }) => (
              <div key={title} className="rounded-2xl border border-border bg-card p-6">
                <div className={`inline-flex items-center justify-center w-11 h-11 rounded-xl ${color} mb-4`}>
                  <Icon className="h-5 w-5" />
                </div>
                <h3 className="font-bold text-lg mb-2">{title}</h3>
                <p className="text-sm text-muted-foreground leading-relaxed">{desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* ── How it works ── */}
        <section id="how-it-works" className="bg-muted/40 border-y border-border py-20">
          <div className="mx-auto max-w-4xl px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl md:text-4xl font-bold mb-3">Up and running in minutes</h2>
              <p className="text-muted-foreground text-lg">No app to download. Works in any browser.</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
              {[
                {
                  step: '1',
                  title: 'Create a free account',
                  desc: 'Sign up with your email. Takes under a minute — no credit card needed.',
                  color: 'bg-teal-600',
                },
                {
                  step: '2',
                  title: 'Add your children',
                  desc: 'Enter each child\'s name and grade. One parent account covers all your kids.',
                  color: 'bg-emerald-600',
                },
                {
                  step: '3',
                  title: 'Watch & learn',
                  desc: 'Each subject starts with a short curated YouTube video matched to that day\'s topic.',
                  color: 'bg-green-600',
                },
                {
                  step: '4',
                  title: 'Quiz & track',
                  desc: 'After the video, a 5-question quiz checks understanding. Results appear instantly in your Parent Dashboard.',
                  color: 'bg-green-700',
                },
              ].map(({ step, title, desc, color }) => (
                <div key={step} className="flex flex-col items-center text-center gap-4">
                  <div className={`w-14 h-14 rounded-2xl ${color} text-white flex items-center justify-center text-2xl font-extrabold shadow-lg`}>
                    {step}
                  </div>
                  <div>
                    <h3 className="font-bold text-lg mb-1">{title}</h3>
                    <p className="text-muted-foreground text-sm leading-relaxed">{desc}</p>
                  </div>
                </div>
              ))}
            </div>

            <div className="text-center mt-10">
              <Button asChild size="lg" className="px-10">
                <Link href="/auth">Create Free Account →</Link>
              </Button>
            </div>
          </div>
        </section>

        {/* ── Grades coverage ── */}
        <section className="mx-auto max-w-5xl px-4 py-20">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold mb-3">Covering all grades K–12</h2>
            <p className="text-muted-foreground text-lg">
              Content for more grades is added regularly.
            </p>
          </div>

          <div className="flex flex-wrap justify-center gap-4">
            {GRADE_GROUPS.map((group) => (
              <div key={group.label} className="rounded-2xl border border-border bg-card p-5 min-w-32">
                <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wide mb-3">
                  {group.label}
                </p>
                <div className="flex flex-wrap gap-2">
                  {group.grades.map((g, idx) => {
                    const ready = Array.isArray(group.ready) ? group.ready[idx] : group.ready;
                    return (
                      <div
                        key={g}
                        className={`relative w-10 h-10 rounded-xl flex items-center justify-center text-sm font-bold border-2 ${
                          ready
                            ? 'bg-primary text-primary-foreground border-primary'
                            : 'bg-muted text-muted-foreground border-border'
                        }`}
                      >
                        {g}
                        {ready && (
                          <span className="absolute -top-1 -right-1 w-4 h-4 bg-green-500 rounded-full flex items-center justify-center">
                            <CheckCircle className="h-3 w-3 text-white" />
                          </span>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>

          <p className="text-center text-sm text-muted-foreground mt-6">
            <span className="inline-flex items-center gap-1.5">
              <span className="w-3 h-3 rounded-sm bg-primary inline-block" /> Available now
            </span>
            <span className="mx-3 text-border">·</span>
            <span className="inline-flex items-center gap-1.5">
              <span className="w-3 h-3 rounded-sm bg-muted border border-border inline-block" /> Coming soon
            </span>
          </p>
        </section>

        {/* ── Subjects ── */}
        <section className="bg-gradient-to-br from-teal-600 via-emerald-600 to-green-700 text-white py-20">
          <div className="mx-auto max-w-5xl px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl md:text-4xl font-bold mb-3">Subjects for every stage</h2>
              <p className="text-white/70 text-lg">From reading and numbers to physics and economics.</p>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
              {[
                { name: 'Language Arts', icon: '📖', grades: 'K–8' },
                { name: 'Mathematics', icon: '🔢', grades: 'K–12' },
                { name: 'Science', icon: '🔬', grades: 'K–10' },
                { name: 'Social Studies', icon: '🌍', grades: 'K–8' },
                { name: 'Physics', icon: '⚡', grades: 'Gr 11–12' },
                { name: 'Chemistry', icon: '🧪', grades: 'Gr 11–12' },
                { name: 'Biology', icon: '🌱', grades: 'Gr 11–12' },
                { name: 'History & Geography', icon: '🗺️', grades: 'Gr 9–12' },
              ].map(({ name, icon, grades }) => (
                <div key={name} className="bg-white/10 backdrop-blur rounded-xl p-4 flex flex-col gap-1">
                  <span className="text-2xl">{icon}</span>
                  <p className="font-semibold text-sm leading-tight">{name}</p>
                  <p className="text-xs text-white/60">{grades}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* ── Social proof / trust ── */}
        <section className="mx-auto max-w-5xl px-4 py-20">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold mb-3">Built for Canadian families</h2>
            <p className="text-muted-foreground text-lg max-w-xl mx-auto">
              GradesBooster is designed around the Ontario curriculum with plans to expand to all provinces and US states.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              {
                icon: Globe,
                color: 'text-purple-600',
                title: 'Ontario Curriculum',
                desc: 'All content is mapped to official Ontario curriculum expectations by grade and strand.',
              },
              {
                icon: Star,
                color: 'text-yellow-500',
                title: 'COPPA & PIPEDA Safe',
                desc: 'No accounts for children under 13. All data is stored securely under the parent account.',
              },
              {
                icon: CheckCircle,
                color: 'text-green-600',
                title: 'Two Learning Modes',
                desc: 'Summer Vacation mode for intensive review. Year-Round mode for steady daily practice.',
              },
            ].map(({ icon: Icon, color, title, desc }) => (
              <div key={title} className="rounded-2xl border border-border bg-card p-6 flex gap-4">
                <Icon className={`h-6 w-6 shrink-0 mt-0.5 ${color}`} />
                <div>
                  <h3 className="font-bold mb-1">{title}</h3>
                  <p className="text-sm text-muted-foreground leading-relaxed">{desc}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* ── FAQ ── */}
        <section id="faq" className="bg-muted/40 border-y border-border py-20">
          <div className="mx-auto max-w-3xl px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl md:text-4xl font-bold mb-3">Frequently asked questions</h2>
              <p className="text-muted-foreground text-lg">Everything parents want to know.</p>
            </div>
            <div className="bg-card rounded-2xl border border-border px-6 divide-y divide-border">
              {FAQS.map((faq) => (
                <FAQItem key={faq.q} q={faq.q} a={faq.a} />
              ))}
            </div>
          </div>
        </section>

        {/* ── Final CTA ── */}
        <section className="mx-auto max-w-3xl px-4 py-24 text-center">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-primary text-primary-foreground mb-6 shadow-lg">
            <GraduationCap className="h-8 w-8" />
          </div>
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Start boosting grades today
          </h2>
          <p className="text-muted-foreground text-lg mb-8 max-w-lg mx-auto">
            Free forever. No credit card. Takes 60 seconds to set up.
          </p>
          <Button asChild size="lg" className="px-12 text-base font-bold">
            <Link href="/auth">Create Your Free Account →</Link>
          </Button>
        </section>
      </main>

      {/* ── Footer ── */}
      <footer className="border-t border-border bg-card">
        <div className="mx-auto max-w-6xl px-4 py-10 flex flex-col md:flex-row items-center justify-between gap-4">
          <Link href="/">
            <Image src="/logo.svg" alt="GradesBooster" width={140} height={33} />
          </Link>
          <div className="flex gap-6 text-sm text-muted-foreground">
            <a href="#faq" className="hover:text-foreground transition-colors">FAQ</a>
            <Link href="/privacy" className="hover:text-foreground transition-colors">Privacy Policy</Link>
            <Link href="/auth" className="hover:text-foreground transition-colors">Sign In</Link>
          </div>
          <p className="text-xs text-muted-foreground">
            © {new Date().getFullYear()} GradesBooster. Ontario, Canada.
          </p>
        </div>
      </footer>

    </div>
  );
}
