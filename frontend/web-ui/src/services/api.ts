import { ENDPOINTS } from './config'

export interface ChatRequest {
  message: string
  session_id: string
  language: string
}

export interface ChatResponse {
  response: string
  session_id: string
  language: string
}

export interface HealthResponse {
  status: string
  version: string
  ollama_connected: boolean
  vector_store_ready: boolean
}

export interface CodeReviewRequest {
  code: string
  language: string
}

export interface CodeReviewResponse {
  summary: string
  issues: { message?: string; severity?: string }[]
  suggestions: string[]
  corrected_code?: string | null
}

export async function checkHealth(): Promise<HealthResponse> {
  const resp = await fetch(ENDPOINTS.health)
  if (!resp.ok) throw new Error(`Health check failed: ${resp.status}`)
  return resp.json()
}

export async function chat(request: ChatRequest): Promise<ChatResponse> {
  const resp = await fetch(ENDPOINTS.chat, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request),
  })
  if (!resp.ok) {
    const err = await resp.text()
    throw new Error(`Chat API error (${resp.status}): ${err}`)
  }
  return resp.json()
}

export async function reviewCode(request: CodeReviewRequest): Promise<CodeReviewResponse> {
  const resp = await fetch(ENDPOINTS.codeReview, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request),
  })
  if (!resp.ok) throw new Error(`Code review failed: ${resp.status}`)
  return resp.json()
}
