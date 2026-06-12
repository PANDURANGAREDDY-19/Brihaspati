import CourseCard from '../components/CourseCard'
import { courseCategories } from '../data/mockData'

function Home() {
  return (
    <section className="space-y-12">
      <div className="grid gap-8 xl:grid-cols-[1.2fr_0.8fr]">
        <article className="glass-panel card overflow-hidden p-10">
          <span className="text-sm uppercase tracking-[0.28em] text-emerald-300/80">Learn Skills That Matter</span>
          <h1 className="mt-5 text-4xl font-semibold leading-tight text-white sm:text-5xl">
            Master Programming, English, and Telugu through interactive learning.
          </h1>
          <p className="mt-6 max-w-2xl text-base text-slate-300 sm:text-lg">
            CodeMentor AI brings the structure of a modern education platform with the energy of a creative learning studio. Explore courses, track your progress, and build confidence every day.
          </p>
          <div className="mt-10 flex flex-col gap-4 sm:flex-row">
            <button className="rounded-full bg-gradient-to-r from-violet-500 to-emerald-400 px-8 py-4 text-sm font-semibold text-white transition hover:brightness-110">
              Start Learning
            </button>
            <button className="rounded-full border border-white/10 bg-white/5 px-8 py-4 text-sm font-semibold text-white transition hover:bg-white/10">
              Explore Courses
            </button>
          </div>
        </article>

        <div className="space-y-6">
          <div className="glass-panel card p-8">
            <p className="text-sm uppercase tracking-[0.24em] text-emerald-300/80">Fast track your goals</p>
            <h2 className="mt-4 text-3xl font-semibold">From beginner to confident learner.</h2>
            <p className="mt-4 text-slate-300">Flexible lessons, guided practice, and progress tracking designed for every learner.</p>
          </div>
          <div className="glass-panel card p-8">
            <div className="flex items-center justify-between gap-4">
              <div>
                <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Latest growth</p>
                <p className="mt-3 text-3xl font-semibold text-white">+24%</p>
              </div>
              <div className="rounded-3xl bg-white/5 px-4 py-3 text-slate-200">Weekly momentum</div>
            </div>
            <div className="mt-7 grid gap-4 sm:grid-cols-2">
              <div className="rounded-3xl bg-slate-900/80 p-5">
                <p className="text-sm text-slate-400">Programming learners</p>
                <p className="mt-3 text-2xl font-semibold text-white">1.4k</p>
              </div>
              <div className="rounded-3xl bg-slate-900/80 p-5">
                <p className="text-sm text-slate-400">Language learners</p>
                <p className="mt-3 text-2xl font-semibold text-white">980</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div>
        <div className="flex items-center justify-between gap-4">
          <div>
            <p className="text-sm uppercase tracking-[0.24em] text-emerald-300/80">Featured learning tracks</p>
            <h2 className="mt-2 text-3xl font-semibold">Courses built for growth</h2>
          </div>
          <span className="text-sm text-slate-400">Updated weekly with new topics</span>
        </div>

        <div className="mt-8 feature-grid">
          {courseCategories.map((category) => (
            <CourseCard key={category.title} title={category.title} description={category.description} topics={category.topics} accent={category.accent} />
          ))}
        </div>
      </div>
    </section>
  )
}

export default Home
