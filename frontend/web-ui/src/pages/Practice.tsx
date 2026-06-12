import { practiceCards } from '../data/mockData'

function Practice() {
  return (
    <section className="space-y-10">
      <div className="glass-panel card p-10">
        <span className="text-sm uppercase tracking-[0.28em] text-emerald-300/80">Practice Lab</span>
        <h1 className="mt-4 text-4xl font-semibold">Build confidence with practical exercises.</h1>
        <p className="mt-4 max-w-2xl text-slate-300">Choose a learning stream and get immediate hands-on practice through mock quizzes and interactive challenges.</p>
      </div>

      <div className="grid gap-6 lg:grid-cols-3">
        {practiceCards.map((card) => (
          <article key={card.title} className="glass-panel card p-8 transition hover:-translate-y-1 hover:shadow-glow">
            <div className={`inline-flex rounded-full bg-gradient-to-r ${card.accent} px-3 py-2 text-sm font-semibold text-white`}>
              {card.title}
            </div>
            <h2 className="mt-6 text-2xl font-semibold">{card.title}</h2>
            <p className="mt-3 text-slate-300">{card.description}</p>
            <ul className="mt-6 space-y-3 text-slate-200">
              {card.items.map((item) => (
                <li key={item} className="flex items-center gap-3 rounded-2xl bg-white/5 px-4 py-3">
                  <span className="text-emerald-300">•</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </article>
        ))}
      </div>
    </section>
  )
}

export default Practice
