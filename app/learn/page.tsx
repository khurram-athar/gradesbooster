'use client';

import { useEffect, useState, useCallback, Suspense } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import Link from 'next/link';
import { useAuth } from '@/components/auth-provider';
import { loadKids, loadKidResults, saveResult } from '@/lib/firestore';
import { Nav } from '@/components/nav';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Alert, AlertDescription } from '@/components/ui/alert';
import {
  AVAILABLE_GRADES,
  SUBJECT_LABELS,
  type KidProfile,
  type DayContent,
  type SubjectContent,
  type QuizResult,
} from '@/types';
import {
  ChevronLeft,
  ChevronRight,
  CheckCircle,
  ExternalLink,
  BookOpen,
  Trophy,
} from 'lucide-react';

import grade0 from '@/data/grade0';
import grade1 from '@/data/grade1';
import grade2 from '@/data/grade2';
import grade3 from '@/data/grade3';
import grade4 from '@/data/grade4';
import grade5 from '@/data/grade5';
import grade6 from '@/data/grade6';
import grade7 from '@/data/grade7';
import grade8 from '@/data/grade8';
import grade9 from '@/data/grade9';
import grade10 from '@/data/grade10';
import grade11 from '@/data/grade11';
import grade12 from '@/data/grade12';

const CURRICULUM_MAP: Record<number, DayContent[]> = {
  0: grade0, 1: grade1, 2: grade2, 3: grade3, 4: grade4,
  5: grade5, 6: grade6, 7: grade7, 8: grade8, 9: grade9,
  10: grade10, 11: grade11, 12: grade12,
};
function loadCurriculum(grade: number): DayContent[] {
  return CURRICULUM_MAP[grade] ?? [];
}

/** Extract YouTube video ID from a full URL or bare ID */
function youtubeId(url: string): string {
  const match = url.match(/(?:v=|youtu\.be\/|embed\/)([A-Za-z0-9_-]{11})/);
  return match ? match[1] : url;
}

/** Build the iframe src URL for a subject.
 *  - If content.videoUrl is already a full embed URL → use it directly.
 *  - If content.videoUrl has a video ID / watch URL → standard embed.
 *  - Otherwise → YouTube search embed matched to the topic title + grade.
 */
function buildVideoEmbedUrl(content: SubjectContent, grade: number): string {
  if (content.videoUrl) {
    if (content.videoUrl.includes('/embed/') || content.videoUrl.includes('listType=search')) {
      return content.videoUrl;
    }
    return `https://www.youtube.com/embed/${youtubeId(content.videoUrl)}?rel=0&modestbranding=1`;
  }
  const gradeStr = grade === 0 ? 'kindergarten' : `grade ${grade}`;
  const query = encodeURIComponent(`${content.title} ${gradeStr} educational`);
  return `https://www.youtube.com/embed?listType=search&list=${query}&rel=0&modestbranding=1`;
}

/** Build the "Watch on YouTube" fallback link URL */
function buildVideoLinkUrl(content: SubjectContent, grade: number): string {
  if (content.videoUrl && !content.videoUrl.includes('listType=search')) {
    return content.videoUrl.includes('/embed/')
      ? content.videoUrl.replace('/embed/', '/watch?v=')
      : content.videoUrl;
  }
  const gradeStr = grade === 0 ? 'kindergarten' : `grade ${grade}`;
  const query = encodeURIComponent(`${content.title} ${gradeStr} educational`);
  return `https://www.youtube.com/results?search_query=${query}`;
}

function scoreColor(pct: number) {
  if (pct >= 80) return 'text-green-600';
  if (pct >= 60) return 'text-yellow-600';
  return 'text-red-500';
}

function scoreBg(pct: number) {
  if (pct >= 80) return 'bg-green-100 text-green-800 border-green-200';
  if (pct >= 60) return 'bg-yellow-100 text-yellow-800 border-yellow-200';
  return 'bg-red-100 text-red-800 border-red-200';
}

// ── Subject Quiz ────────────────────────────────────────────────────────────

function SubjectQuiz({
  content,
  savedScore,
  onComplete,
  onNext,
  isLast,
}: {
  content: SubjectContent;
  savedScore: number | null;
  onComplete: (score: number, total: number) => void;
  onNext: () => void;
  isLast: boolean;
}) {
  // SubjectPanel remounts this component with a fresh key whenever the
  // active subject changes, so these only need to be set once at mount —
  // they must NOT reset in response to savedScore changing after our own
  // submit (that used to wipe `answers` right after the Firestore write
  // completed, which zeroed out the score display even on a perfect quiz).
  const [answers, setAnswers] = useState<(number | null)[]>(content.quiz.map(() => null));
  const [submitted, setSubmitted] = useState(savedScore !== null);

  const canSubmit = answers.every((a) => a !== null) && !submitted;

  function handleSubmit() {
    if (!canSubmit) return;
    const score = answers.reduce(
      (acc, a, i) => acc + (a === content.quiz[i].answer ? 1 : 0),
      0,
    );
    setSubmitted(true);
    onComplete(score, content.quiz.length);
  }

  const liveScore = submitted
    ? answers.reduce((acc: number, a, i) => acc + (a === content.quiz[i].answer ? 1 : 0), 0)
    : null;
  const displayScore = liveScore ?? savedScore;
  const total = content.quiz.length;

  return (
    <div className="space-y-5">
      {/* Quiz header */}
      <div className="flex items-center justify-between border-t border-border pt-5">
        <p className="text-xs font-semibold uppercase tracking-widest text-muted-foreground">
          Quiz — {total} questions
        </p>
        {displayScore !== null && (
          <Badge variant="outline" className={`text-sm font-semibold ${scoreBg((displayScore / total) * 100)}`}>
            {displayScore}/{total}
          </Badge>
        )}
      </div>

      {/* Questions */}
      {content.quiz.map((q, qi) => (
        <div key={qi} className="space-y-2.5">
          <p className="font-medium text-base leading-snug">
            {qi + 1}. {q.q}
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
            {q.options.map((opt, oi) => {
              const isSelected = answers[qi] === oi;
              const isCorrect = oi === q.answer;
              let cls =
                'w-full text-left px-4 py-3 rounded-lg border-2 text-sm font-medium transition-all ';
              if (!submitted) {
                cls += isSelected
                  ? 'border-primary bg-primary/10 text-primary shadow-sm'
                  : 'border-border bg-card hover:border-primary/40 hover:bg-muted/50';
              } else {
                if (isCorrect)
                  cls += 'border-green-500 bg-green-50 text-green-800 cursor-default';
                else if (isSelected && !isCorrect)
                  cls += 'border-red-400 bg-red-50 text-red-700 line-through cursor-default';
                else
                  cls += 'border-border text-muted-foreground opacity-60 cursor-default';
              }
              return (
                <button
                  key={oi}
                  type="button"
                  className={cls}
                  disabled={submitted}
                  onClick={() => {
                    if (submitted) return;
                    setAnswers((prev) => { const c = [...prev]; c[qi] = oi; return c; });
                  }}
                >
                  <span className="inline-flex items-center gap-2">
                    <span className={`w-5 h-5 rounded-full border-2 flex items-center justify-center shrink-0 text-xs ${
                      !submitted && isSelected ? 'border-primary bg-primary text-primary-foreground'
                        : submitted && isCorrect ? 'border-green-500 bg-green-500 text-white'
                        : submitted && isSelected && !isCorrect ? 'border-red-400 bg-red-400 text-white'
                        : 'border-current opacity-40'
                    }`}>
                      {String.fromCharCode(65 + oi)}
                    </span>
                    {opt}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      ))}

      {/* Submit / result row */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center gap-3 pt-1">
        {!submitted ? (
          <Button size="lg" disabled={!canSubmit} onClick={handleSubmit} className="w-full sm:w-auto">
            Submit Quiz
          </Button>
        ) : (
          <>
            <div className={`flex items-center gap-2 font-semibold text-base ${scoreColor((displayScore! / total) * 100)}`}>
              <CheckCircle className="h-5 w-5" />
              {displayScore === total ? 'Perfect score! 🎉' : `${displayScore} out of ${total} correct`}
            </div>
            <Button
              size="lg"
              onClick={onNext}
              className="w-full sm:w-auto ml-auto"
            >
              {isLast ? '✓ Day Complete' : 'Next Subject →'}
            </Button>
          </>
        )}
      </div>
    </div>
  );
}

// ── Subject panel ───────────────────────────────────────────────────────────

function SubjectPanel({
  content,
  grade,
  savedScore,
  onComplete,
  onNext,
  isLast,
}: {
  content: SubjectContent;
  grade: number;
  savedScore: number | null;
  onComplete: (score: number, total: number) => void;
  onNext: () => void;
  isLast: boolean;
}) {
  return (
    <div className="space-y-5">
      {/* Title */}
      <div>
        <p className="text-xs font-semibold uppercase tracking-widest text-muted-foreground mb-1">
          {SUBJECT_LABELS[content.subject] ?? content.subject}
        </p>
        <h2 className="text-2xl font-bold leading-tight">{content.title}</h2>
      </div>

      {/* Summary */}
      <p className="text-base text-foreground leading-relaxed">{content.summary}</p>

      {/* YouTube embed — topic-matched video for every day */}
      <div className="space-y-2">
        <p className="text-xs font-semibold uppercase tracking-widest text-muted-foreground">
          Watch the video, then take the quiz below
        </p>
        <div className="rounded-xl overflow-hidden border border-border shadow-sm">
          <div className="relative w-full" style={{ paddingBottom: '56.25%' }}>
            <iframe
              src={buildVideoEmbedUrl(content, grade)}
              title={content.title}
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              className="absolute inset-0 w-full h-full"
            />
          </div>
        </div>
        <a
          href={buildVideoLinkUrl(content, grade)}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-1.5 text-xs text-muted-foreground hover:text-primary transition-colors"
        >
          <ExternalLink className="h-3 w-3" />
          Search YouTube if video doesn&apos;t load
        </a>
      </div>

      {/* Resource button — shown alongside or when no video */}
      {content.resourceUrl && (
        <a
          href={content.resourceUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-2 px-5 py-3 rounded-lg border-2 border-primary bg-primary/5 text-primary font-semibold hover:bg-primary/10 transition-colors text-sm"
        >
          <ExternalLink className="h-4 w-4 shrink-0" />
          {content.resourceLabel || 'Open Learning Resource'}
          <span className="ml-1 text-xs font-normal opacity-70">↗ opens in new tab</span>
        </a>
      )}

      {/* Quiz */}
      <SubjectQuiz
        content={content}
        savedScore={savedScore}
        onComplete={onComplete}
        onNext={onNext}
        isLast={isLast}
      />
    </div>
  );
}

// ── Main learn page ─────────────────────────────────────────────────────────

function LearnContent() {
  const { user, loading } = useAuth();
  const router = useRouter();
  const params = useSearchParams();

  const kidId = params.get('kid') ?? '';
  const grade = parseInt(params.get('grade') ?? '0', 10);
  const mode = params.get('mode') ?? 'summer';

  const [kid, setKid] = useState<KidProfile | null>(null);
  const [curriculum, setCurriculum] = useState<DayContent[]>([]);
  const [results, setResults] = useState<Map<string, QuizResult>>(new Map());
  const [currentDay, setCurrentDay] = useState(0);
  const [currentSubject, setCurrentSubject] = useState(0);
  const [pageLoading, setPageLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!loading && !user) router.replace('/auth');
  }, [user, loading, router]);

  useEffect(() => {
    if (!user || !kidId || !grade) return;
    async function init() {
      try {
        const kids = await loadKids(user!.uid);
        const found = kids.find((k) => k.id === kidId);
        if (!found) { router.replace('/home'); return; }
        setKid(found);

        const curric = loadCurriculum(grade);
        const res = await loadKidResults(user!.uid, kidId, grade);
        setCurriculum(curric);
        setResults(res);

        // Open on first incomplete day
        const firstIncompleteDay = curric.findIndex((day) =>
          day.subjects.some((s) => !res.has(`g${grade}_d${day.day}_${s.subject}`)),
        );
        const dayIdx = firstIncompleteDay === -1 ? 0 : firstIncompleteDay;
        setCurrentDay(dayIdx);

        // Open on first incomplete subject of that day
        const daySubjects = curric[dayIdx]?.subjects ?? [];
        const firstIncompleteSub = daySubjects.findIndex(
          (s) => !res.has(`g${grade}_d${curric[dayIdx].day}_${s.subject}`),
        );
        setCurrentSubject(firstIncompleteSub === -1 ? 0 : firstIncompleteSub);
      } catch (e) {
        setError('Failed to load. Please try again.');
        console.error(e);
      } finally {
        setPageLoading(false);
      }
    }
    init();
  }, [user, kidId, grade, router]);

  const handleQuizComplete = useCallback(
    async (subject: string, dayContent: DayContent, score: number, total: number) => {
      if (!user || !kidId) return;
      await saveResult(user.uid, kidId, grade, dayContent.day, dayContent.label, subject, score, total);
      const id = `g${grade}_d${dayContent.day}_${subject}`;
      setResults((prev) => {
        const next = new Map(prev);
        next.set(id, {
          grade: String(grade), day: dayContent.day, dayLabel: dayContent.label,
          subject, score, total, date: new Date().toISOString().slice(0, 10), updatedAt: Date.now(),
        });
        return next;
      });
    },
    [user, kidId, grade],
  );

  // ── Loading / error states ────────────────────────────────────────────────

  if (loading || !user || pageLoading) {
    return (
      <div className="flex flex-col min-h-screen">
        <Nav />
        <div className="flex-1 flex items-center justify-center">
          <p className="text-muted-foreground text-sm">Loading…</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col min-h-screen">
        <Nav />
        <div className="flex-1 mx-auto max-w-2xl px-4 py-8">
          <Alert variant="destructive"><AlertDescription>{error}</AlertDescription></Alert>
          <Button asChild className="mt-4" variant="outline"><Link href="/home">← Back</Link></Button>
        </div>
      </div>
    );
  }

  if (curriculum.length === 0) {
    return (
      <div className="flex flex-col min-h-screen">
        <Nav />
        <div className="flex-1 mx-auto max-w-2xl px-4 py-8 text-center">
          <BookOpen className="h-12 w-12 mx-auto text-muted-foreground mb-4" />
          <h2 className="text-xl font-semibold mb-2">Curriculum Coming Soon</h2>
          <p className="text-muted-foreground text-sm mb-6">
            We&apos;re preparing Grade {grade} content. Check back soon!
          </p>
          <Button asChild variant="outline"><Link href="/home">← Back to My Kids</Link></Button>
        </div>
      </div>
    );
  }

  const day = curriculum[currentDay];
  if (!day) return null;

  // Progress
  const totalSubjects = curriculum.reduce((a, d) => a + d.subjects.length, 0);
  const completedSubjects = curriculum.reduce(
    (a, d) => a + d.subjects.filter((s) => results.has(`g${grade}_d${d.day}_${s.subject}`)).length, 0,
  );
  const progressPct = Math.round((completedSubjects / totalSubjects) * 100);
  const dayComplete = day.subjects.every((s) => results.has(`g${grade}_d${day.day}_${s.subject}`));

  const activeSubject = day.subjects[currentSubject];
  const activeResultId = activeSubject ? `g${grade}_d${day.day}_${activeSubject.subject}` : '';
  const activeResult = results.get(activeResultId);

  // Jump to a day and land on its first incomplete subject (or the first
  // subject if the whole day is already done).
  function goToDay(newDayIdx: number) {
    const target = curriculum[newDayIdx];
    const firstIncompleteSub = target
      ? target.subjects.findIndex((s) => !results.has(`g${grade}_d${target.day}_${s.subject}`))
      : -1;
    setCurrentDay(newDayIdx);
    setCurrentSubject(firstIncompleteSub === -1 ? 0 : firstIncompleteSub);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function goNextSubject() {
    if (currentSubject < day.subjects.length - 1) {
      setCurrentSubject((s) => s + 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (currentDay < curriculum.length - 1) {
      goToDay(currentDay + 1);
    }
  }

  return (
    <div className="flex flex-col min-h-screen bg-muted/20">
      <Nav />

      <main className="flex-1 mx-auto w-full max-w-3xl px-4 py-6">

        {/* Back + meta */}
        <div className="flex items-center justify-between mb-4">
          <Button asChild variant="ghost" size="sm" className="-ml-2 text-muted-foreground">
            <Link href="/home">← My Kids</Link>
          </Button>
          <span className="text-sm text-muted-foreground">
            {mode === 'summer' ? 'Summer Plan' : 'Year-Round'} · Grade {grade}
          </span>
        </div>

        {/* Kid name + overall progress */}
        <div className="mb-5">
          <div className="flex items-center justify-between mb-2">
            <h1 className="text-2xl font-bold">{kid?.name}</h1>
            <span className="text-sm font-medium text-muted-foreground">{progressPct}% done</span>
          </div>
          <div className="h-2 rounded-full bg-muted overflow-hidden">
            <div className="h-full bg-primary rounded-full transition-all duration-500" style={{ width: `${progressPct}%` }} />
          </div>
        </div>

        {/* Day navigation bar */}
        <div className="flex items-center gap-3 mb-6 bg-card border border-border rounded-xl px-4 py-3">
          <Button variant="ghost" size="icon" disabled={currentDay === 0}
            onClick={() => goToDay(currentDay - 1)}>
            <ChevronLeft className="h-4 w-4" />
          </Button>

          <div className="flex-1 text-center">
            <p className="font-semibold text-sm">{day.label}</p>
            {day.reviewNote
              ? <p className="text-xs text-muted-foreground">{day.reviewNote}</p>
              : <p className="text-xs text-muted-foreground">Day {day.day} of {curriculum.length}</p>
            }
          </div>

          <Button variant="ghost" size="icon" disabled={currentDay === curriculum.length - 1}
            onClick={() => goToDay(currentDay + 1)}>
            <ChevronRight className="h-4 w-4" />
          </Button>
        </div>

        {/* Day complete banner */}
        {dayComplete && (
          <Alert className="mb-5 border-green-200 bg-green-50">
            <Trophy className="h-4 w-4 text-green-600" />
            <AlertDescription className="text-green-800 font-semibold">
              All done for today! Great work.
              {currentDay < curriculum.length - 1 && (
                <button className="ml-2 underline font-normal"
                  onClick={() => goToDay(currentDay + 1)}>
                  Continue to Day {day.day + 1} →
                </button>
              )}
            </AlertDescription>
          </Alert>
        )}

        {/* Subject selector tabs */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-6">
          {day.subjects.map((s, idx) => {
            const rid = `g${grade}_d${day.day}_${s.subject}`;
            const done = results.has(rid);
            const score = results.get(rid)?.score;
            const total = results.get(rid)?.total ?? 1;
            const isActive = idx === currentSubject;
            return (
              <button
                key={s.subject}
                onClick={() => setCurrentSubject(idx)}
                className={`relative flex flex-col items-start gap-0.5 px-3 py-2.5 rounded-xl border-2 text-left transition-all ${
                  isActive
                    ? 'border-primary bg-primary text-primary-foreground shadow-sm'
                    : done
                    ? 'border-green-200 bg-green-50 text-green-800 hover:border-green-400'
                    : 'border-border bg-card text-foreground hover:border-primary/50 hover:bg-muted/50'
                }`}
              >
                <span className="text-xs font-semibold leading-tight">
                  {SUBJECT_LABELS[s.subject] ?? s.subject}
                </span>
                {done ? (
                  <span className={`text-xs ${isActive ? 'text-primary-foreground/80' : 'text-green-600 font-medium'}`}>
                    {score}/{total} ✓
                  </span>
                ) : (
                  <span className={`text-xs ${isActive ? 'text-primary-foreground/60' : 'text-muted-foreground'}`}>
                    Not started
                  </span>
                )}
              </button>
            );
          })}
        </div>

        {/* Active subject content */}
        {activeSubject && (
          <div className="bg-card border border-border rounded-2xl p-6 shadow-sm">
            <SubjectPanel
              key={`${currentDay}-${currentSubject}`}
              content={activeSubject}
              grade={grade}
              savedScore={activeResult?.score ?? null}
              onComplete={(score, total) => handleQuizComplete(activeSubject.subject, day, score, total)}
              onNext={goNextSubject}
              isLast={currentSubject === day.subjects.length - 1 && currentDay === curriculum.length - 1}
            />
          </div>
        )}
      </main>
    </div>
  );
}

export default function LearnPage() {
  return (
    <Suspense fallback={
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-muted-foreground text-sm">Loading…</p>
      </div>
    }>
      <LearnContent />
    </Suspense>
  );
}
