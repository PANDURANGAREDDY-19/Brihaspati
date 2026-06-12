const isDev = import.meta.env.DEV

export const API_BASE_URL = isDev
  ? (import.meta.env.VITE_API_URL || 'http://localhost:8000')
  : (import.meta.env.VITE_API_URL || 'http://localhost:8000')

export const ENDPOINTS = {
  health: `${API_BASE_URL}/health`,
  chat: `${API_BASE_URL}/api/v1/chat`,
  teach: `${API_BASE_URL}/api/v1/teach`,
  codeReview: `${API_BASE_URL}/api/v1/code/review`,
  codeExecute: `${API_BASE_URL}/api/v1/code/execute`,
} as const
