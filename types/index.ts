export type SubjectKey =
  | 'Language'
  | 'Math'
  | 'Science'
  | 'SocialStudies'
  | 'Physics'
  | 'Chemistry'
  | 'Biology'
  | 'History'
  | 'Geography'
  | 'English'
  | 'Functions'
  | 'AdvancedFunctions'
  | 'Calculus';

export const SUBJECT_LABELS: Record<SubjectKey, string> = {
  Language: 'Language Arts',
  Math: 'Mathematics',
  Science: 'Science',
  SocialStudies: 'Social Studies',
  Physics: 'Physics',
  Chemistry: 'Chemistry',
  Biology: 'Biology',
  History: 'History',
  Geography: 'Geography',
  English: 'English',
  Functions: 'Functions',
  AdvancedFunctions: 'Advanced Functions',
  Calculus: 'Calculus & Vectors',
};

export const SUBJECT_COLORS: Record<SubjectKey, string> = {
  Language: 'bg-blue-500',
  Math: 'bg-green-600',
  Science: 'bg-purple-600',
  SocialStudies: 'bg-orange-500',
  Physics: 'bg-indigo-600',
  Chemistry: 'bg-teal-600',
  Biology: 'bg-emerald-600',
  History: 'bg-amber-600',
  Geography: 'bg-rose-500',
  English: 'bg-sky-600',
  Functions: 'bg-violet-600',
  AdvancedFunctions: 'bg-fuchsia-600',
  Calculus: 'bg-red-600',
};

export const SUBJECT_BORDER_COLORS: Record<SubjectKey, string> = {
  Language: 'border-l-blue-500',
  Math: 'border-l-green-600',
  Science: 'border-l-purple-600',
  SocialStudies: 'border-l-orange-500',
  Physics: 'border-l-indigo-600',
  Chemistry: 'border-l-teal-600',
  Biology: 'border-l-emerald-600',
  History: 'border-l-amber-600',
  Geography: 'border-l-rose-500',
  English: 'border-l-sky-600',
  Functions: 'border-l-violet-600',
  AdvancedFunctions: 'border-l-fuchsia-600',
  Calculus: 'border-l-red-600',
};

export interface QuizQuestion {
  q: string;
  options: string[];
  answer: number;
}

export interface SubjectContent {
  subject: SubjectKey;
  title: string;
  summary: string;
  resourceUrl: string;
  resourceLabel: string;
  videoUrl?: string;       // optional YouTube video URL for embedding
  quiz: QuizQuestion[];
}

export interface DayContent {
  day: number;
  label: string;
  reviewNote?: string;
  subjects: SubjectContent[];
}

export type LearningMode = 'summer' | 'yearround';

export interface KidProfile {
  id: string;
  name: string;
  grade: number;
  country: 'CA' | 'US';
  province: string;
  createdAt: number;
}

export interface QuizResult {
  grade: string;
  day: number;
  dayLabel: string;
  subject: string;
  score: number;
  total: number;
  date: string;
  updatedAt: number;
}

export interface DashboardRow {
  date: string;
  kidId: string;
  kidName: string;
  grade: string;
  day: string;
  subject: string;
  score: number;
  total: number;
  pct: number;
}

// Grades that currently have curriculum content
export const AVAILABLE_GRADES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
