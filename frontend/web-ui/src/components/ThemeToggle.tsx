type ThemeToggleProps = {
  theme: 'light' | 'dark'
  onToggle: () => void
}

function ThemeToggle({ theme, onToggle }: ThemeToggleProps) {
  return (
    <button
      onClick={onToggle}
      className="inline-flex items-center gap-3 rounded-full border border-white/10 bg-slate-900/80 px-4 py-3 text-sm text-slate-100 transition hover:border-emerald-400/40 hover:bg-slate-800/90"
    >
      <span>{theme === 'dark' ? '🌙' : '☀️'}</span>
      <span>{theme === 'dark' ? 'Dark mode' : 'Light mode'}</span>
    </button>
  )
}

export default ThemeToggle
