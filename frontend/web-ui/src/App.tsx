import { NavLink, Route, Routes } from 'react-router-dom'
import About from './pages/About'
import Courses from './pages/Courses'
import Dashboard from './pages/Dashboard'
import Home from './pages/Home'
import Practice from './pages/Practice'
import Footer from './components/Footer'
import Chatbot from './components/Chatbot'

const navItems = [
  { label: 'Home', path: '/' },
  { label: 'Courses', path: '/courses' },
  { label: 'Dashboard', path: '/dashboard' },
  { label: 'Practice', path: '/practice' },
  { label: 'About', path: '/about' },
]

function App() {
  return (
    <div className="theme-dark min-h-screen bg-slate-950 text-slate-100">
      <div className="relative overflow-hidden">
        <div className="pointer-events-none absolute inset-x-0 top-0 h-72 bg-radialGlow opacity-70 blur-3xl" />
        <div className="relative z-10 mx-auto max-w-7xl px-6 py-6 lg:px-8">
          <header className="flex flex-col gap-5 border-b border-white/10 pb-5 md:flex-row md:items-center md:justify-between">
            <div className="flex items-center gap-4">
              <div className="flex h-12 w-12 items-center justify-center rounded-3xl bg-gradient-to-br from-violet-500 to-emerald-400 text-xl font-bold shadow-glow shadow-violet-500/20">
                CM
              </div>
              <div>
                <p className="text-sm uppercase tracking-[0.3em] text-emerald-300/80">CodeMentor AI</p>
                <h1 className="text-2xl font-semibold sm:text-3xl">Learn. Practice. Build. Grow.</h1>
              </div>
            </div>

            <div className="flex flex-col gap-4 sm:flex-row sm:items-center">
              <div className="relative w-full max-w-sm">
                <span className="pointer-events-none absolute inset-y-0 left-4 flex items-center text-slate-400">🔍</span>
                <input
                  type="search"
                  placeholder="Search courses, topics, lessons"
                  className="w-full rounded-3xl border border-white/10 bg-slate-900/80 py-3 pl-12 pr-4 text-sm text-slate-100 outline-none transition hover:border-white/20 focus:border-emerald-400/60 focus:ring-2 focus:ring-emerald-400/20"
                />
              </div>
            </div>
          </header>

          <nav className="mt-6 flex flex-wrap gap-3 text-sm font-medium text-slate-300">
            {navItems.map((item) => (
              <NavLink
                key={item.path}
                to={item.path}
                className={({ isActive }) =>
                  `rounded-full px-4 py-2 transition ${
                    isActive ? 'bg-white/10 text-white shadow-glow' : 'hover:bg-white/5 hover:text-white'
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
        </div>
      </div>

      <main className="mx-auto max-w-7xl px-6 pb-16 pt-8 lg:px-8">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/courses" element={<Courses />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/practice" element={<Practice />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </main>

      <Chatbot />
      <Footer />
    </div>
  )
}

export default App
