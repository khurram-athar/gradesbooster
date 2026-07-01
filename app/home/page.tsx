'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useAuth } from '@/components/auth-provider';
import { loadKids } from '@/lib/firestore';
import { Nav } from '@/components/nav';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { AVAILABLE_GRADES, type KidProfile } from '@/types';
import { Plus, BookOpen, Clock } from 'lucide-react';

function gradeLabel(g: number): string {
  if (g === 0) return 'Kindergarten';
  return `Grade ${g}`;
}

export default function HomePage() {
  const { user, loading } = useAuth();
  const router = useRouter();
  const [kids, setKids] = useState<KidProfile[]>([]);
  const [kidsLoading, setKidsLoading] = useState(true);

  useEffect(() => {
    if (!loading && !user) router.replace('/auth');
  }, [user, loading, router]);

  useEffect(() => {
    if (!user) return;
    loadKids(user.uid)
      .then(setKids)
      .finally(() => setKidsLoading(false));
  }, [user]);

  if (loading || !user) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-muted-foreground text-sm">Loading…</p>
      </div>
    );
  }

  return (
    <div className="flex flex-col min-h-screen">
      <Nav />

      <main className="flex-1 mx-auto w-full max-w-5xl px-4 py-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-2xl font-bold">My Kids</h1>
            <p className="text-sm text-muted-foreground mt-0.5">
              Select a child to start their daily lesson.
            </p>
          </div>
          <Button asChild>
            <Link href="/kids">
              <Plus className="h-4 w-4 mr-1.5" />
              Add Child
            </Link>
          </Button>
        </div>

        {kidsLoading ? (
          <p className="text-sm text-muted-foreground">Loading children…</p>
        ) : kids.length === 0 ? (
          <Card className="border-dashed bg-muted/30">
            <CardContent className="flex flex-col items-center justify-center py-16 text-center gap-4">
              <div className="w-14 h-14 rounded-full bg-muted flex items-center justify-center">
                <BookOpen className="h-7 w-7 text-muted-foreground" />
              </div>
              <div>
                <p className="font-semibold text-lg">No children added yet</p>
                <p className="text-sm text-muted-foreground mt-1">
                  Add your first child to get started with daily learning.
                </p>
              </div>
              <Button asChild>
                <Link href="/kids">
                  <Plus className="h-4 w-4 mr-1.5" />
                  Add a Child
                </Link>
              </Button>
            </CardContent>
          </Card>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {kids.map((kid) => {
              const hasContent = AVAILABLE_GRADES.includes(kid.grade);
              return (
                <Card
                  key={kid.id}
                  className={`transition-shadow ${hasContent ? 'hover:shadow-md' : 'opacity-70'}`}
                >
                  <CardHeader className="pb-3">
                    <div className="flex items-start justify-between">
                      <div>
                        <CardTitle className="text-xl">{kid.name}</CardTitle>
                        <CardDescription className="mt-0.5">
                          {gradeLabel(kid.grade)} · {kid.province}, {kid.country}
                        </CardDescription>
                      </div>
                      {!hasContent && (
                        <Badge variant="secondary" className="shrink-0 text-xs">
                          Coming soon
                        </Badge>
                      )}
                    </div>
                  </CardHeader>
                  <CardContent className="pt-0">
                    {hasContent ? (
                      <div className="flex gap-2">
                        <Button asChild size="sm" className="flex-1">
                          <Link href={`/learn?kid=${kid.id}&grade=${kid.grade}&mode=summer`}>
                            <Clock className="h-3.5 w-3.5 mr-1.5" />
                            Summer Plan
                          </Link>
                        </Button>
                        <Button asChild size="sm" variant="outline" className="flex-1">
                          <Link href={`/learn?kid=${kid.id}&grade=${kid.grade}&mode=yearround`}>
                            Year-Round
                          </Link>
                        </Button>
                      </div>
                    ) : (
                      <p className="text-xs text-muted-foreground">
                        Curriculum for {gradeLabel(kid.grade)} is being prepared.
                      </p>
                    )}
                  </CardContent>
                </Card>
              );
            })}

            {/* Add another child card */}
            <Card className="border-dashed bg-muted/20 hover:bg-muted/40 transition-colors">
              <Link href="/kids" className="block h-full">
                <CardContent className="flex flex-col items-center justify-center h-full py-8 text-center gap-2">
                  <div className="w-10 h-10 rounded-full border-2 border-dashed border-muted-foreground/30 flex items-center justify-center">
                    <Plus className="h-5 w-5 text-muted-foreground" />
                  </div>
                  <p className="text-sm text-muted-foreground">Add another child</p>
                </CardContent>
              </Link>
            </Card>
          </div>
        )}
      </main>
    </div>
  );
}
