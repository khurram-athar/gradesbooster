'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import type { User } from 'firebase/auth';
import { useAuth } from '@/components/auth-provider';
import { isAdminEmail } from '@/lib/admin';
import { Nav } from '@/components/nav';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Alert, AlertDescription } from '@/components/ui/alert';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { RefreshCw, Inbox } from 'lucide-react';

interface FeedbackItem {
  id: string;
  uid: string | null;
  email: string | null;
  message: string;
  category: string;
  page: string | null;
  createdAt: string | null;
}

const CATEGORY_LABELS: Record<string, string> = {
  bug: 'Something is broken',
  content: 'Curriculum or quiz content',
  idea: 'Feature idea',
  other: 'Other',
};

function categoryBadgeClass(category: string) {
  switch (category) {
    case 'bug':
      return 'bg-red-100 text-red-800 border-red-200';
    case 'content':
      return 'bg-yellow-100 text-yellow-800 border-yellow-200';
    case 'idea':
      return 'bg-green-100 text-green-800 border-green-200';
    default:
      return 'bg-muted text-muted-foreground border-border';
  }
}

function formatDate(iso: string | null) {
  if (!iso) return '—';
  return new Date(iso).toLocaleString(undefined, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
  });
}

// Pure data fetch -- deliberately does not call setState itself, so it can
// be safely called both from an effect (auto-load on mount) and from an
// event handler (manual refresh) without either caller referencing a
// shared memoized function that sets state.
async function fetchFeedback(user: User): Promise<{ items?: FeedbackItem[]; error?: string }> {
  try {
    const token = await user.getIdToken();
    const res = await fetch('/api/admin/feedback', {
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = await res.json();
    if (!res.ok) return { error: data.error || 'Failed to load feedback.' };
    return { items: data.feedback };
  } catch (err) {
    console.error(err);
    return { error: 'Failed to load feedback.' };
  }
}

export default function AdminFeedbackPage() {
  const { user, loading } = useAuth();
  const router = useRouter();
  const [items, setItems] = useState<FeedbackItem[] | null>(null);
  const [fetching, setFetching] = useState(false);
  const [error, setError] = useState('');

  const isAdmin = !loading && !!user && isAdminEmail(user.email);

  useEffect(() => {
    if (!loading && !user) {
      router.replace('/auth');
    }
  }, [loading, user, router]);

  useEffect(() => {
    if (!user || !isAdmin) return;
    let cancelled = false;
    (async () => {
      setFetching(true);
      setError('');
      const result = await fetchFeedback(user);
      if (cancelled) return;
      if (result.error) {
        setError(result.error);
        setItems([]);
      } else {
        setItems(result.items ?? []);
      }
      setFetching(false);
    })();
    return () => {
      cancelled = true;
    };
  }, [user, isAdmin]);

  const handleRefresh = async () => {
    if (!user) return;
    setFetching(true);
    setError('');
    const result = await fetchFeedback(user);
    if (result.error) {
      setError(result.error);
      setItems([]);
    } else {
      setItems(result.items ?? []);
    }
    setFetching(false);
  };

  if (loading || !user) {
    return (
      <div className="flex flex-col min-h-screen">
        <Nav />
        <div className="flex-1 flex items-center justify-center text-muted-foreground text-sm">
          Loading…
        </div>
      </div>
    );
  }

  if (!isAdmin) {
    return (
      <div className="flex flex-col min-h-screen">
        <Nav />
        <main className="flex-1 mx-auto w-full max-w-xl px-4 py-10">
          <Alert variant="destructive">
            <AlertDescription>
              You don&apos;t have access to this page.
            </AlertDescription>
          </Alert>
        </main>
      </div>
    );
  }

  return (
    <div className="flex flex-col min-h-screen bg-muted/20">
      <Nav />
      <main className="flex-1 mx-auto w-full max-w-5xl px-4 py-10">
        <div className="flex items-center justify-between gap-3 mb-6">
          <div className="flex items-center gap-3">
            <div className="flex items-center justify-center w-10 h-10 rounded-xl bg-primary/10 text-primary shrink-0">
              <Inbox className="h-5 w-5" />
            </div>
            <div>
              <h1 className="text-xl font-bold">Feedback inbox</h1>
              <p className="text-sm text-muted-foreground">
                {items ? `${items.length} message${items.length === 1 ? '' : 's'}` : 'Loading…'}
              </p>
            </div>
          </div>
          <Button variant="outline" size="sm" onClick={handleRefresh} disabled={fetching} className="gap-1.5">
            <RefreshCw className={`h-4 w-4 ${fetching ? 'animate-spin' : ''}`} />
            Refresh
          </Button>
        </div>

        {error && (
          <Alert variant="destructive" className="mb-4">
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        <Card>
          <CardHeader>
            <CardTitle>All feedback</CardTitle>
          </CardHeader>
          <CardContent>
            {!items || items.length === 0 ? (
              <p className="text-sm text-muted-foreground py-8 text-center">
                {items ? 'No feedback yet.' : 'Loading…'}
              </p>
            ) : (
              <div className="overflow-x-auto">
                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead className="whitespace-nowrap">Date</TableHead>
                      <TableHead>Category</TableHead>
                      <TableHead>Message</TableHead>
                      <TableHead>From</TableHead>
                      <TableHead>Page</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {items.map((item) => (
                      <TableRow key={item.id}>
                        <TableCell className="whitespace-nowrap text-sm text-muted-foreground">
                          {formatDate(item.createdAt)}
                        </TableCell>
                        <TableCell>
                          <Badge variant="outline" className={categoryBadgeClass(item.category)}>
                            {CATEGORY_LABELS[item.category] ?? item.category}
                          </Badge>
                        </TableCell>
                        <TableCell className="max-w-md whitespace-pre-wrap text-sm">
                          {item.message}
                        </TableCell>
                        <TableCell className="text-sm text-muted-foreground whitespace-nowrap">
                          {item.email ?? '—'}
                        </TableCell>
                        <TableCell className="text-sm text-muted-foreground whitespace-nowrap">
                          {item.page ?? '—'}
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </div>
            )}
          </CardContent>
        </Card>
      </main>
    </div>
  );
}
