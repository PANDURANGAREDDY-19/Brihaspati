export type CourseCategory = {
  title: string
  description: string
  topics: string[]
  accent: string
}

export type DashboardStat = {
  label: string
  value: string
  detail: string
  accent: string
}

export type LessonModule = {
  title: string
  duration: string
  status: 'Completed' | 'In progress' | 'Locked'
}

export type PracticeCard = {
  title: string
  description: string
  items: string[]
  accent: string
}

export const courseCategories: CourseCategory[] = [
  {
    title: 'Programming',
    description: 'Learn the most in-demand coding languages and build modern applications.',
    topics: ['Python', 'Java', 'C', 'C++', 'JavaScript', 'HTML', 'CSS'],
    accent: 'from-indigo-500 via-violet-500 to-fuchsia-500',
  },
  {
    title: 'English',
    description: 'Build communication confidence with grammar, vocabulary, and speaking practice.',
    topics: ['Grammar', 'Vocabulary', 'Speaking', 'Writing', 'Reading'],
    accent: 'from-emerald-500 via-teal-500 to-cyan-500',
  },
  {
    title: 'Telugu',
    description: 'Master Telugu reading and writing through guided exercises and stories.',
    topics: ['Reading', 'Writing', 'Vocabulary', 'Grammar', 'Spoken Telugu'],
    accent: 'from-orange-400 via-rose-500 to-pink-500',
  },
]

export const dashboardStats: DashboardStat[] = [
  { label: 'Courses Enrolled', value: '8', detail: '3 new this month', accent: 'from-cyan-500 to-blue-500' },
  { label: 'Lessons Completed', value: '142', detail: '20 completed this week', accent: 'from-violet-500 to-fuchsia-500' },
  { label: 'Learning Streak', value: '16 days', detail: 'Keep the momentum going', accent: 'from-emerald-500 to-lime-500' },
  { label: 'Progress', value: '72%', detail: 'Overall achievement', accent: 'from-amber-400 to-orange-500' },
]

export const courseDetailModules: LessonModule[] = [
  { title: 'Module 1: Variables', duration: '18 min', status: 'Completed' },
  { title: 'Module 2: Loops', duration: '24 min', status: 'Completed' },
  { title: 'Module 3: Functions', duration: '31 min', status: 'In progress' },
  { title: 'Module 4: OOP', duration: '42 min', status: 'Locked' },
]

export const practiceCards: PracticeCard[] = [
  {
    title: 'Programming Practice',
    description: 'Sharpen logic with MCQs and coding challenges.',
    items: ['MCQs', 'Coding Exercises'],
    accent: 'from-sky-500 to-indigo-500',
  },
  {
    title: 'English Practice',
    description: 'Improve fluency with grammar and vocabulary tests.',
    items: ['Grammar Questions', 'Vocabulary Tests'],
    accent: 'from-emerald-500 to-teal-500',
  },
  {
    title: 'Telugu Practice',
    description: 'Practice reading and spoken Telugu in engaging formats.',
    items: ['Vocabulary', 'Reading Exercises'],
    accent: 'from-orange-400 to-pink-500',
  },
]

export const teamMembers = [
  { name: 'Ananya Rao', role: 'Learning Designer' },
  { name: 'Ravi Kumar', role: 'Product Lead' },
  { name: 'Priya Mehta', role: 'Content Strategist' },
  { name: 'Dev Patel', role: 'Experience Engineer' },
]
