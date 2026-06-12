type CourseCardProps = {
  title: string
  description: string
  topics: string[]
  accent: string
}

function CourseCard({ title, description, topics, accent }: CourseCardProps) {
  return (
    <article className="glass-panel card p-8 transition hover:-translate-y-1 hover:shadow-glow">
      <div className={`mb-4 inline-flex rounded-full bg-gradient-to-r ${accent} bg-clip-text px-3 py-2 text-sm font-semibold text-transparent`}>
        {title}
      </div>
      <h2 className="text-2xl font-semibold tracking-tight">{title} Essentials</h2>
      <p className="mt-3 text-slate-300">{description}</p>
      <div className="mt-6 grid gap-2 text-sm text-slate-200">
        {topics.map((topic) => (
          <span key={topic} className="inline-flex rounded-full bg-white/5 px-3 py-2">
            {topic}
          </span>
        ))}
      </div>
      <div className="mt-8 flex items-center justify-between">
        <span className="text-xs uppercase tracking-[0.2em] text-slate-500">Designed for learners</span>
        <span className="rounded-full bg-white/5 px-3 py-1 text-xs text-slate-300">Explore</span>
      </div>
    </article>
  )
}

export default CourseCard
