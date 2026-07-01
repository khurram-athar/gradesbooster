'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/components/auth-provider';
import { loadKids, loadAllKidResults } from '@/lib/firestore';
import { Nav } from '@/components/nav';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
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
import { Download, TrendingUp } from 'lucide-react';

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

export default function DashboardPage() {
  const { user, loading } = useAuth();
  const router = useRouter();
  const [kids, setKids] = useState<KidProfile[]>([]);
  const [allResults, setAllResults] = useState<Map<string, Map<string, QuizResult>>>(new Map());
  const [pageLoading, setPageLoading] = useState(true);
  const [filterKid, setFilterKid] = useState<string>('all');
  const [filterToday, setFilterToday] = useState(false);

  useEffect(() => {
    if (!loading && !user) router.replace('/auth');
  }, [user, loading, router]);

  useEffect(() => {
    if (!user) return;
    async function load() {
      const kidsData = await loadKids(user!.uid);
      setKids(kidsData);
      const results = await loadAllKidResults(user!.uid, kidsData);
      setAllResults(results);
      setPageLoading(false);
    }
    load();
  }, [user]);

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

  return (
    <div className="flex flex-col min-h-screen">
      <Nav />

      <main className="flex-1 mx-auto w-full max-w-5xl px-4 py-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-2xl font-bold">Parent Dashboard</h1>
            <p className="text-sm text-muted-foreground mt-0.5">Track each child&apos;s progress across all subjects.</p>
          </div>
          {filteredRows.length > 0 && (
            <Button variant="outline" size="sm" onClick={downloadCSV}>
              <Download className="h-4 w-4 mr-1.5" />
              Export CSV
            </Button>
          )}
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
                      <div className="flex items-center gap-2">
                        <TrendingUp className="h-4 w-4 text-muted-foreground" />
                        <span className={`text-lg font-bold ${avg >= 80 ? 'text-green-600' : avg >= 60 ? 'text-yellow-600' : 'text-red-500'}`}>
                          {avg}%
                        </span>
                        <span className="text-xs text-muted-foreground">avg · {count} quizzes</span>
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
    </div>
  );
}
