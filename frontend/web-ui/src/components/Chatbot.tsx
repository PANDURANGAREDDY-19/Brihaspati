import { useEffect, useMemo, useRef, useState, type KeyboardEvent } from 'react'

type Message = {
  sender: 'bot' | 'user'
  text: string
}

const initialMessages: Message[] = [
  {
    sender: 'bot',
    text: "Hello! I'm CodeMentor AI. How can I help you learn Programming, English, or Telugu today?",
  },
]

const botReplies: { keywords: string[]; text: string }[] = [
  {
    keywords: ['python', 'java', 'cplusplus', 'javascript', 'html', 'css', 'c++', 'c'],
    text: 'I can help you explore syntax, write sample code, or compare programming topics. What would you like to practice first?',
  },
  {
    keywords: ['grammar', 'vocabulary', 'speaking', 'writing', 'reading'],
    text: 'Let’s build your language skills with clear examples and practice questions. Which area should we focus on?',
  },
  {
    keywords: ['telugu', 'telugu grammar', 'spoke', 'reading'],
    text: 'Telugu learning is fun with structured exercises. I can help you practice reading, writing, and vocabulary.',
  },
]

function Chatbot() {
  const [open, setOpen] = useState(false)
  const [input, setInput] = useState('')
  const [messages, setMessages] = useState<Message[]>(initialMessages)
  const [sending, setSending] = useState(false)
  const scrollRef = useRef<HTMLDivElement | null>(null)

  const handleSend = () => {
    const trimmed = input.trim()
    if (!trimmed) return
    const userMessage: Message = { sender: 'user', text: trimmed }
    setMessages((prev) => [...prev, userMessage])
    setInput('')
    setSending(true)

    setTimeout(() => {
      const lower = trimmed.toLowerCase()
      const reply = botReplies.find((item) => item.keywords.some((keyword) => lower.includes(keyword)))?.text ??
        'That sounds great. I can guide you with course recommendations, practice suggestions, and quick concept explanations. What would you like to do next?'
      setMessages((prev) => [...prev, { sender: 'bot', text: reply }])
      setSending(false)
    }, 650)
  }

  const handleKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter') {
      event.preventDefault()
      handleSend()
    }
  }

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: 'smooth' })
  }, [messages, open])

  const buttonLabel = useMemo(() => (open ? 'Close' : 'Chat'), [open])

  return (
    <div className="fixed right-6 bottom-6 z-50 flex flex-col items-end gap-4">
      {open && (
        <div className="glass-panel w-[360px] max-w-full rounded-[32px] border border-white/10 shadow-glow shadow-black/40">
          <div className="flex items-center justify-between border-b border-white/10 px-5 py-4">
            <div>
              <p className="text-sm uppercase tracking-[0.24em] text-emerald-300/80">CodeMentor AI</p>
              <h3 className="mt-1 text-lg font-semibold text-white">AI Learning Assistant</h3>
            </div>
            <span className="inline-flex h-10 w-10 items-center justify-center rounded-2xl bg-white/5 text-lg">🤖</span>
          </div>

          <div ref={scrollRef} className="max-h-[360px] space-y-4 overflow-y-auto px-5 py-4 text-sm text-slate-200">
            {messages.map((message, index) => (
              <div key={`${message.sender}-${index}`} className={`rounded-3xl p-4 ${message.sender === 'bot' ? 'bg-slate-900/90' : 'ml-auto max-w-[85%] bg-emerald-500/10 text-slate-100'}`}>
                <p className="text-xs uppercase tracking-[0.2em] text-slate-400">{message.sender === 'bot' ? 'Mentor' : 'You'}</p>
                <p className="mt-2 leading-6">{message.text}</p>
              </div>
            ))}
          </div>

          <div className="border-t border-white/10 px-4 py-4">
            <div className="flex gap-3">
              <input
                value={input}
                onChange={(event) => setInput(event.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Ask a question or start a topic..."
                className="w-full rounded-2xl border border-white/10 bg-slate-950/90 px-4 py-3 text-sm text-slate-100 outline-none focus:border-emerald-400/60 focus:ring-2 focus:ring-emerald-400/15"
              />
              <button
                type="button"
                onClick={handleSend}
                disabled={sending}
                className="rounded-2xl bg-gradient-to-r from-violet-500 to-emerald-400 px-5 py-3 text-sm font-semibold text-white transition hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {sending ? 'Sending...' : 'Send'}
              </button>
            </div>
          </div>
        </div>
      )}

      <button
        type="button"
        onClick={() => setOpen((prev) => !prev)}
        className="inline-flex items-center gap-3 rounded-full bg-gradient-to-r from-violet-500 to-emerald-400 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-500/20 transition hover:-translate-y-0.5"
      >
        <span>{buttonLabel}</span>
        <span className="rounded-full bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em]">AI</span>
      </button>
    </div>
  )
}

export default Chatbot
