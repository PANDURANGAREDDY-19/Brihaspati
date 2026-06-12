import { teamMembers } from '../data/mockData'

function About() {
  return (
    <section className="space-y-10">
      <div className="glass-panel card p-10">
        <span className="text-sm uppercase tracking-[0.28em] text-emerald-300/80">About CodeMentor AI</span>
        <h1 className="mt-4 text-4xl font-semibold">A smarter way to learn programming and languages.</h1>
        <p className="mt-4 max-w-3xl text-slate-300">Our mission is to deliver a welcoming, modern learning experience for students who want to grow with structured content, useful practice, and clear progress tracking.</p>
      </div>

      <div className="grid gap-6 xl:grid-cols-3">
        <div className="glass-panel card p-8">
          <h2 className="text-2xl font-semibold">Mission</h2>
          <p className="mt-4 text-slate-300">Empower learners with scalable, easy-to-follow lessons that bridge coding and language learning in one polished platform.</p>
        </div>
        <div className="glass-panel card p-8">
          <h2 className="text-2xl font-semibold">Vision</h2>
          <p className="mt-4 text-slate-300">Create a trusted digital campus where every student gains skills for school, career, and everyday communication.</p>
        </div>
        <div className="glass-panel card p-8">
          <h2 className="text-2xl font-semibold">Benefits</h2>
          <ul className="mt-4 space-y-3 text-slate-300">
            <li>Personalized learning paths</li>
            <li>Practice-driven mastery</li>
            <li>Progress tracking and motivation</li>
          </ul>
        </div>
      </div>

      <div className="glass-panel card p-10">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h2 className="text-3xl font-semibold">Meet your learning team</h2>
            <p className="mt-3 text-slate-300">A small team building big learning experiences with clarity and care.</p>
          </div>
          <span className="rounded-full bg-white/5 px-4 py-2 text-sm text-slate-200">Contact us anytime</span>
        </div>

        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {teamMembers.map((member) => (
            <div key={member.name} className="rounded-3xl border border-white/5 bg-slate-950/50 p-6">
              <p className="text-lg font-semibold text-white">{member.name}</p>
              <p className="mt-2 text-slate-400">{member.role}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="glass-panel card p-10">
        <h2 className="text-3xl font-semibold">Contact</h2>
        <p className="mt-4 text-slate-300">Get in touch with the CodeMentor AI team for course guidance or feedback.</p>
        <div className="mt-8">
          <div className="rounded-3xl bg-slate-950/60 p-6">
            <p className="text-sm uppercase tracking-[0.24em] text-slate-500">Email</p>
            <p className="mt-3 text-lg font-semibold text-white">munindrasripathi@gmail.com</p>
          </div>
        </div>
      </div>
    </section>
  )
}

export default About
