import DashboardCard from '../components/DashboardCard'
import ProgressBar from '../components/ProgressBar'
import { courseDetailModules, dashboardStats } from '../data/mockData'

function Dashboard() {
  return (
    <section className="space-y-10">
      <div className="glass-panel card p-10">
        <span className="text-sm uppercase tracking-[0.28em] text-emerald-300/80">Learning Dashboard</span>
        <h1 className="mt-4 text-4xl font-semibold">Your progress at a glance.</h1>
        <p className="mt-4 max-w-2xl text-slate-300">Monitor enrolled courses, completed lessons, streaks, and overall progress from one premium dashboard.</p>
      </div>

      <div className="grid gap-6 lg:grid-cols-4">
        {dashboardStats.map((stat) => (
          <DashboardCard key={stat.label} label={stat.label} value={stat.value} detail={stat.detail} accent={stat.accent} />
        ))}
      </div>

      <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
        <div className="glass-panel card p-10">
          <div className="flex items-center justify-between">
            <div>
              <span className="text-sm uppercase tracking-[0.28em] text-slate-400">Active course</span>
              <h2 className="mt-3 text-3xl font-semibold">Python Programming</h2>
            </div>
            <span className="rounded-full bg-white/5 px-4 py-2 text-sm text-slate-200">Intermediate</span>
          </div>
          <p className="mt-6 text-slate-300">A hands-on course for developers who want to build real applications with Python. Learn key concepts, best practices, and apply them in practical exercises.</p>
          <div className="mt-8 space-y-6">
            {courseDetailModules.map((module) => (
              <div key={module.title} className="rounded-3xl border border-white/5 bg-slate-950/50 p-5">
                <div className="flex items-center justify-between gap-3">
                  <div>
                    <h3 className="font-semibold text-white">{module.title}</h3>
                    <p className="text-sm text-slate-400">{module.duration}</p>
                  </div>
                  <span className="rounded-full bg-white/5 px-3 py-1 text-sm text-slate-200">{module.status}</span>
                </div>
              </div>
            ))}
          </div>
          <div className="mt-8">
            <div className="flex items-center justify-between gap-4">
              <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Course progress</p>
              <p className="text-sm font-semibold text-white">72%</p>
            </div>
            <ProgressBar value={72} />
          </div>
        </div>

        <div className="glass-panel card p-10">
          <p className="text-sm uppercase tracking-[0.24em] text-slate-500">Learning habits</p>
          <div className="mt-8 grid gap-5">
            <div className="rounded-3xl border border-white/5 bg-slate-950/50 p-6">
              <h3 className="text-xl font-semibold text-white">Weekly streak</h3>
              <p className="mt-3 text-slate-300">You've learned every day for 16 days. Keep the streak alive with short lessons and practice.</p>
            </div>
            <div className="rounded-3xl border border-white/5 bg-slate-950/50 p-6">
              <h3 className="text-xl font-semibold text-white">Upcoming session</h3>
              <p className="mt-3 text-slate-300">Tomorrow: English conversation practice and Telugu alphabet review.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Dashboard
