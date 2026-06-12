import CourseCard from '../components/CourseCard'
import { courseCategories } from '../data/mockData'

function Courses() {
  return (
    <section className="space-y-10">
      <div className="glass-panel card p-10">
        <span className="text-sm uppercase tracking-[0.28em] text-emerald-300/80">Learning Categories</span>
        <h1 className="mt-4 text-4xl font-semibold">Explore the courses that power your future.</h1>
        <p className="mt-4 max-w-2xl text-slate-300">Browse programming, English, and Telugu learning paths created for meaningful progress across every skill level.</p>
      </div>

      <div className="feature-grid">
        {courseCategories.map((category) => (
          <CourseCard key={category.title} title={category.title} description={category.description} topics={category.topics} accent={category.accent} />
        ))}
      </div>
    </section>
  )
}

export default Courses
