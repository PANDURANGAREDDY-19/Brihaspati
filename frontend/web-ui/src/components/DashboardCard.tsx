type DashboardCardProps = {
  label: string
  value: string
  detail: string
  accent: string
}

function DashboardCard({ label, value, detail, accent }: DashboardCardProps) {
  return (
    <div className="glass-panel card p-6 shadow-lg transition hover:-translate-y-1">
      <span className={`inline-flex rounded-full bg-gradient-to-r ${accent} px-3 py-1 text-xs font-semibold uppercase tracking-[0.2em] text-white/90`}>{label}</span>
      <p className="mt-6 text-4xl font-semibold tracking-tight text-white">{value}</p>
      <p className="mt-2 text-sm text-slate-400">{detail}</p>
    </div>
  )
}

export default DashboardCard
