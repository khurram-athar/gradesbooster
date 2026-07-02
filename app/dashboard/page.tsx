'use client';

import { useEffect, useState, useRef } from 'react';
import { useRouter } from 'next/navigation';
import { EmailAuthProvider, reauthenticateWithCredential } from 'firebase/auth';
import { auth } from '@/lib/firebase';
import { useAuth } from '@/components/auth-provider';
import { loadKids, loadAllKidResults } from '@/lib/firestore';
import { Nav } from '@/components/nav';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import type { KidProfile, QuizResult, DashboardRow } from '@/types';
import { Download, TrendingUp, Lock, Eye, EyeOff, Sparkles, X } from 'lucide-react';

function pctBadge(pct: number) {
  if (pct >= 80) return 'bg-green-100 text-green-800 border-green-200';
  if (pct >= 60) return 'bg-yellow-100 text-yellow-800 border-yellow-200';
  return 'bg-red-100 text-red-800 border-red-200';
}

function buildRows(
  kids: KidProfile[],
  allResults: Map<string, Map<string, QuizResult>>,
): DashboardRow[] {
  const rows: DashboardRow[] = [];
  kids.forEach((kid) => {
    const kidResults = allResults.get(kid.id);
    if (!kidResults) return;
    kidResults.forEach((result) => {
      const pct = Math.round((result.score / result.total) * 100);
      rows.push({
        date: result.date,
        kidId: kid.id,
        kidName: kid.name,
        grade: `Grade ${result.grade}`,
        day: result.dayLabel,
        subject: result.subject,
        score: result.score,
        total: result.total,
        pct,
      });
    });
  });
  rows.sort((a, b) => b.date.localeCompare(a.date));
  return rows;
}

function kidAvgScore(kidId: string, allResults: Map<string, Map<string, QuizResult>>) {
  const results = allResults.get(kidId);
  if (!results || results.size === 0) return null;
  let total = 0, count = 0;
  results.forEach((r) => {
    total += (r.score / r.total) * 100;
    count++;
  });
  return Math.round(total / count);
}

// ── Re-auth modal ────────────────────────────────────────────

function ReAuthGate({ onSuccess }: { onSuccess: () => void }) {
  const [password, setPassword] = useState('');
  const [showPw, setShowPw] = useState(false);
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError('');
    setBusy(true);
    try {
      const currentUser = auth.currentUser;
      if (!currentUser?.email) throw new Error('No signed-in user');
      const credential = EmailAuthProvider.credential(currentUser.email, password);
      await reauthenticateWithCredential(currentUser, credential);
      onSuccess();
    } catch {
      setError('Incorrect password. Please try again.');
      setPassword('');
      inputRef.current?.focus();
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="flex flex-col min-h-screen">
      <Nav />
      <div className="flex-1 flex items-center justify-center px-4">
        <Card className="w-full max-w-sm">
          <CardHeader className="text-center pb-2">
            <div className="mx-auto mb-3 h-12 w-12 rounded-full bg-violet-100 flex items-center justify-center">
              <Lock className="h-5 w-5 text-violet-600" />
            </div>
            <CardTitle className="text-lg">Confirm your identity</CardTitle>
            <p className="text-sm text-muted-foreground mt-1">
              Enter your password to view quiz results.
            </p>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-3">
              <div className="relative">
                <Input
                  ref={inputRef}
                  type={showPw ? 'text' : 'password'}
                  placeholder="Your password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="pr-10"
                  required
                  disabled={busy}
                />
                <button
                  type="button"
                  onClick={() => setShowPw((v) => !v)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-muted-foreground hover:text-foreground"
                  tabIndex={-1}
                >
                  {showPw ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                </button>
              </div>
              {error && (
                <p className="text-sm text-red-600">{error}</p>
              )}
              <Button type="submit" className="w-full" disabled={busy || !password}>
                {busy ? 'Verifying…' : 'View Results'}
              </Button>
            </form>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

// ── AI Assessment modal ──────────────────────────────────────

function AssessmentModal({
  kid,
  results,
  onClose,
}: {
  kid: KidProfile;
  results: Map<string, QuizResult>;
  onClose: () => void;
}) {
  const [report, setReport] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    async function generate() {
      try {
        const resultsList = Array.from(results.values()).map((r) => ({
          subject: r.subject,
          day: r.day,
          dayLabel: r.dayLabel,
          score: r.score,
          total: r.total,
          date: r.date,
        }));

        const res = await fetch('/api/assessment', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ kidName: kid.name, grade: kid.grade, results: resultsList }),
        });

        if (!res.ok) throw new Error('Failed to generate report');
        const data = await res.json();
        setReport(data.report);
      } catch {
        setError('Could not generate report. Please try again.');
      } finally {
        setLoading(false);
      }
    }
    generate();
  }, [kid, results]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4" onClick={onClose}>
      <div
        className="bg-background rounded-2xl border border-border shadow-xl w-full max-w-lg p-6 relative"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={onClose}
          className="absolute top-4 right-4 text-muted-foreground hover:text-foreground"
        >
          <X className="h-5 w-5" />
        </button>

        <div className="flex items-center gap-3 mb-4">
          <div className="h-10 w-10 rounded-xl bg-violet-100 flex items-center justify-center">
            <Sparkles className="h-5 w-5 text-violet-600" />
          </div>
          <div>
            <h2 className="font-bold text-lg">{kid.name}&apos;s End-of-Term Report</h2>
            <p className="text-xs text-muted-foreground">
              Grade {kid.grade === 0 ? 'K' : kid.grade} · AI-generated assessment
            </p>
          </div>
        </div>

        {loading ? (
          <div className="py-10 text-center text-muted-foreground text-sm">
            <Sparkles className="h-6 w-6 mx-auto mb-3 text-violet-400 animate-pulse" />
            Generating personalised report…
          </div>
        ) : error ? (
          <p className="text-red-600 text-sm py-4">{error}</p>
        ) : (
          <div className="space-y-3">
            {report.split('\n\n').filter(Boolean).map((para, i) => (
              <p key={i} className="text-sm leading-relaxed text-foreground">{para}</p>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

// ── Main dashboard ───────────────────────────────────────────

export default function DashboardPage() {
  const { user, loading } = useAuth();
  const router = useRouter();
  const [authed, setAuthed] = useState(false);
  const [kids, setKids] = useState<KidProfile[]>([]);
  const [allResults, setAllResults] = useState<Map<string, Map<string, QuizResult>>>(new Map());
  const [pageLoading, setPageLoading] = useState(true);
  const [filterKid, setFilterKid] = useState<string>('all');
  const [filterToday, setFilterToday] = useState(false);
  const [assessmentKid, setAssessmentKid] = useState<KidProfile | null>(null);

  useEffect(() => {
    if (!loading && !user) router.replace('/auth');
  }, [user, loading, router]);

  useEffect(() => {
    if (!user || !authed) return;
    async function load() {
      const kidsData = await loadKids(user!.uid);
      setKids(kidsData);
      const results = await loadAllKidResults(user!.uid, kidsData);
      setAllResults(results);
      setPageLoading(false);
    }
    load();
  }, [user, authed]);

  if (loading || !user) {
    return (
      <div className="flex flex-col min-h-screen">
        <Nav />
        <div className="flex-1 flex items-center justify-center">
          <p className="text-muted-foreground text-sm">Loading…</p>
        </div>
      </div>
    );
  }

  // Show re-auth gate before any data is displayed
  if (!authed) {
    return <ReAuthGate onSuccess={() => setAuthed(true)} />;
  }

  if (pageLoading) {
    return (
      <div className="flex flex-col min-h-screen">
        <Nav />
        <div className="flex-1 flex items-center justify-center">
          <p className="text-muted-foreground text-sm">Loading results…</p>
        </div>
      </div>
    );
  }

  const today = new Date().toISOString().slice(0, 10);
  const allRows = buildRows(kids, allResults);

  const filteredRows = allRows.filter((r) => {
    if (filterKid !== 'all' && r.kidId !== filterKid) return false;
    if (filterToday && r.date !== today) return false;
    return true;
  });

  function downloadCSV() {
    const header = 'Date,Child,Grade,Day,Subject,Score,Total,Percent\n';
    const body = filteredRows
      .map(
        (r) =>
          `${r.date},"${r.kidName}",${r.grade},"${r.day}",${r.subject},${r.score},${r.total},${r.pct}%`,
      )
      .join('\n');
    const blob = new Blob([header + body], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'gradesbooster-results.csv';
    a.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="flex flex-col min-h-screen">
      <Nav />

      <main className="flex-1 mx-auto w-full max-w-5xl px-4 py-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-2xl font-bold">Parent Dashboard</h1>
            <p className="text-sm text-muted-foreground mt-0.5">Track each child&apos;s progress across all subjects.</p>
          </div>
          <div className="flex items-center gap-2">
            {filteredRows.length > 0 && (
              <Button variant="outline" size="sm" onClick={downloadCSV}>
                <Download className="h-4 w-4 mr-1.5" />
                Export CSV
              </Button>
            )}
            <Button variant="ghost" size="sm" onClick={() => setAuthed(false)}>
              <Lock className="h-4 w-4 mr-1.5" />
              Lock
            </Button>
          </div>
        </div>

        {/* Kid summary cards */}
        {kids.length > 0 && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
            {kids.map((kid) => {
              const avg = kidAvgScore(kid.id, allResults);
              const count = allResults.get(kid.id)?.size ?? 0;
              return (
                <Card key={kid.id}>
                  <CardHeader className="pb-2">
                    <CardTitle className="text-base">{kid.name}</CardTitle>
                    <p className="text-xs text-muted-foreground">Grade {kid.grade}</p>
                  </CardHeader>
                  <CardContent>
                    {avg !== null ? (
                      <div className="space-y-3">
                        <div className="flex items-center gap-2">
                          <TrendingUp className="h-4 w-4 text-muted-foreground" />
                          <span className={`text-lg font-bold ${avg >= 80 ? 'text-green-600' : avg >= 60 ? 'text-yellow-600' : 'text-red-500'}`}>
                            {avg}%
                          </span>
                          <span className="text-xs text-muted-foreground">avg · {count} quizzes</span>
                        </div>
                        <Button
                          size="sm"
                          variant="outline"
                          className="w-full text-xs"
                          onClick={() => setAssessmentKid(kid)}
                        >
                          <Sparkles className="h-3 w-3 mr-1.5 text-violet-500" />
                          AI Term Report
                        </Button>
                      </div>
                    ) : (
                      <p className="text-sm text-muted-foreground">No quizzes yet</p>
                    )}
                  </CardContent>
                </Card>
              );
            })}
          </div>
        )}

        {/* Filters */}
        <div className="flex flex-wrap gap-3 mb-4 items-center">
          <Select value={filterKid} onValueChange={setFilterKid}>
            <SelectTrigger className="w-40">
              <SelectValue placeholder="All children" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All children</SelectItem>
              {kids.map((kid) => (
                <SelectItem key={kid.id} value={kid.id}>{kid.name}</SelectItem>
              ))}
            </SelectContent>
          </Select>

          <Button
            variant={filterToday ? 'default' : 'outline'}
            size="sm"
            onClick={() => setFilterToday((v) => !v)}
          >
            Today only
          </Button>

          <span className="text-sm text-muted-foreground ml-auto">
            {filteredRows.length} result{filteredRows.length !== 1 ? 's' : ''}
          </span>
        </div>

        {/* Results table */}
        {filteredRows.length === 0 ? (
          <Card>
            <CardContent className="py-12 text-center">
              <p className="text-muted-foreground text-sm">
                {allRows.length === 0
                  ? 'No quiz results yet. Start a lesson to see progress here.'
                  : 'No results match the current filters.'}
              </p>
            </CardContent>
          </Card>
        ) : (
          <div className="rounded-lg border border-border overflow-hidden">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Date</TableHead>
                  <TableHead>Child</TableHead>
                  <TableHead>Day</TableHead>
                  <TableHead>Subject</TableHead>
                  <TableHead className="text-right">Score</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {filteredRows.map((row, i) => (
                  <TableRow key={i}>
                    <TableCell className="text-sm text-muted-foreground">{row.date}</TableCell>
                    <TableCell className="font-medium">{row.kidName}</TableCell>
                    <TableCell className="text-sm">{row.day}</TableCell>
                    <TableCell className="text-sm">{row.subject}</TableCell>
                    <TableCell className="text-right">
                      <Badge
                        variant="outline"
                        className={`text-xs font-medium ${pctBadge(row.pct)}`}
                      >
                        {row.score}/{row.total} ({row.pct}%)
                      </Badge>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}
      </main>

      {assessmentKid && (
        <AssessmentModal
          kid={assessmentKid}
          results={allResults.get(assessmentKid.id) ?? new Map()}
          onClose={() => setAssessmentKid(null)}
        />
      )}
    </div>
  );
}
