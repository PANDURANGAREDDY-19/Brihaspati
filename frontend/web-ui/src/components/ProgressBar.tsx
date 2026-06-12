type ProgressBarProps = {
  value: number
}

function ProgressBar({ value }: ProgressBarProps) {
  return (
    <div className="mt-4 h-3 overflow-hidden rounded-full bg-slate-800/80">
      <div className="h-full rounded-full bg-gradient-to-r from-emerald-400 to-cyan-400 transition-all" style={{ width: `${value}%` }} />
    </div>
  )
}

export default ProgressBar
