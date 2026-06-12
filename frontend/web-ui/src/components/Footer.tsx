function Footer() {
  return (
    <footer className="border-t border-white/10 bg-slate-950/70 py-10 text-slate-400">
      <div className="mx-auto flex max-w-7xl flex-col gap-6 px-6 sm:flex-row sm:items-center sm:justify-between lg:px-8">
        <div>
          <p className="font-semibold text-slate-100">CodeMentor AI</p>
          <p className="mt-2 text-sm text-slate-500">An intelligent learning experience for programming, English, and Telugu.</p>
        </div>
        <div className="flex flex-wrap gap-4 text-sm text-slate-400">
          <span>Terms</span>
          <span>Privacy</span>
          <span>Contact</span>
        </div>
      </div>
    </footer>
  )
}

export default Footer
