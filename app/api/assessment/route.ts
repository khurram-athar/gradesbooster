import { NextRequest, NextResponse } from 'next/server';
import Anthropic from '@anthropic-ai/sdk';

// POST /api/assessment
// Body: { kidName: string; grade: number; results: QuizResultSummary[] }
// Returns: { report: string }

export interface QuizResultSummary {
  subject: string;
  day: number;
  dayLabel: string;
  score: number;
  total: number;
  date: string;
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { kidName, grade, results } = body as {
      kidName: string;
      grade: number;
      results: QuizResultSummary[];
    };

    if (!kidName || grade == null || !Array.isArray(results)) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    if (!process.env.ANTHROPIC_API_KEY) {
      return NextResponse.json({ error: 'ANTHROPIC_API_KEY not configured' }, { status: 500 });
    }

    // ── Build a summary per subject ──────────────────────────
    const bySubject: Record<string, { scores: number[]; total: number }> = {};
    for (const r of results) {
      if (!bySubject[r.subject]) bySubject[r.subject] = { scores: [], total: r.total };
      bySubject[r.subject].scores.push(r.score);
    }

    const subjectLines = Object.entries(bySubject).map(([subject, data]) => {
      const avg = data.scores.reduce((a, b) => a + b, 0) / data.scores.length;
      const pct = Math.round((avg / data.total) * 100);
      const quizCount = data.scores.length;
      return `- ${subject}: ${pct}% average across ${quizCount} quiz${quizCount !== 1 ? 'zes' : ''}`;
    });

    const overallScores = results.map((r) => (r.score / r.total) * 100);
    const overallAvg = Math.round(
      overallScores.reduce((a, b) => a + b, 0) / overallScores.length,
    );
    const daysCompleted = new Set(results.map((r) => r.day)).size;

    const prompt = `You are a warm, encouraging educational coach writing an end-of-term assessment for a child's parent.

Child: ${kidName}
Grade: ${grade === 0 ? 'Kindergarten' : `Grade ${grade}`}
Days completed: ${daysCompleted} out of 30
Overall average score: ${overallAvg}%

Subject breakdown:
${subjectLines.join('\n')}

Write a personalised end-of-term assessment report in 3–4 short paragraphs. Include:
1. A warm opening acknowledging the child's effort and what they've completed
2. Specific strengths based on the highest-scoring subjects
3. Gentle encouragement for areas to keep practising (lowest-scoring subjects)
4. A motivating closing statement about the child's progress and readiness for the next grade

Keep the tone warm, specific, and encouraging — this will be read by a parent. Do not use markdown, bullet points, or headers. Write in plain paragraphs.`;

    const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

    const message = await client.messages.create({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 600,
      messages: [{ role: 'user', content: prompt }],
    });

    const report =
      message.content[0].type === 'text' ? message.content[0].text : 'Unable to generate report.';

    return NextResponse.json({ report });
  } catch (err) {
    console.error('[/api/assessment]', err);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
