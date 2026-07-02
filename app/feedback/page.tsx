'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/components/auth-provider';
import { submitFeedback } from '@/lib/firestore';
import { Nav } from '@/components/nav';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Textarea } from '@/components/ui/textarea';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { MessageSquareHeart, CheckCircle2 } from 'lucide-react';

const CATEGORIES = [
  { value: 'bug', label: 'Something is broken' },
  { value: 'content', label: 'Curriculum or quiz content' },
  { value: 'idea', label: 'Feature idea' },
  { value: 'other', label: 'Other' },
];

export default function FeedbackPage() {
  const { user, loading } = useAuth();
  const router = useRouter();
  const [category, setCategory] = useState('bug');
  const [message, setMessage] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!loading && !user) router.replace('/auth');
  }, [loading, user, router]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!user) return;
    if (message.trim().length === 0) {
      setError('Please enter a message before submitting.');
      return;
    }
    setError('');
    setSubmitting(true);
    try {
      await submitFeedback(user.uid, user.email, message.trim(), category);
      setSubmitted(true);
      setMessage('');
    } catch (err) {
      console.error(err);
      setError('Something went wrong sending your feedback. Please try again.');
    } finally {
      setSubmitting(false);
    }
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

  return (
    <div className="flex flex-col min-h-screen bg-muted/20">
      <Nav />
      <main className="flex-1 mx-auto w-full max-w-xl px-4 py-10">
        <div className="flex items-center gap-3 mb-6">
          <div className="flex items-center justify-center w-10 h-10 rounded-xl bg-primary/10 text-primary shrink-0">
            <MessageSquareHeart className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-xl font-bold">Send feedback</h1>
            <p className="text-sm text-muted-foreground">
              Found a bug or have an idea? We read every message.
            </p>
          </div>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Tell us what&apos;s on your mind</CardTitle>
          </CardHeader>
          <CardContent>
            {submitted ? (
              <Alert className="border-green-200 bg-green-50 text-green-900">
                <CheckCircle2 className="h-4 w-4 text-green-600" />
                <AlertDescription className="text-green-900">
                  Thanks — your feedback was sent. We appreciate you taking the time.
                </AlertDescription>
              </Alert>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="space-y-1.5">
                  <label className="text-sm font-medium">Category</label>
                  <Select value={category} onValueChange={setCategory}>
                    <SelectTrigger className="w-full">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      {CATEGORIES.map((c) => (
                        <SelectItem key={c.value} value={c.value}>
                          {c.label}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-1.5">
                  <label className="text-sm font-medium">Message</label>
                  <Textarea
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="What happened, or what would make GradesBooster better for your family?"
                    rows={6}
                    maxLength={4000}
                  />
                </div>

                {error && (
                  <Alert variant="destructive">
                    <AlertDescription>{error}</AlertDescription>
                  </Alert>
                )}

                <Button type="submit" disabled={submitting} className="w-full">
                  {submitting ? 'Sending…' : 'Send feedback'}
                </Button>
              </form>
            )}
          </CardContent>
        </Card>
      </main>
    </div>
  );
}
