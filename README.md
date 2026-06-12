# Brihaspati

> Bilingual Coding Assistant — Teach programming in Telugu and English using Ollama-powered AI agents.

Brihaspati is an open-source AI assistant that helps students learn coding in their native language. It uses local LLMs via Ollama to provide tutoring, code review, problem solving, and bilingual explanations — all without sending data to external APIs.

## Architecture

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  Coding  │     │   Code   │     │ Problem  │     │Bilingual │
│   Tutor  │     │ Reviewer │     │  Solver  │     │  Agent   │
└────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘
     └────────────────┼────────────────┼────────────────┘
                      │     FastAPI    │
                      ▼                ▼
               ┌──────────────────────────┐
               │      Ollama (LLM)        │
               │  llama3.1 / qwen2.5      │
               └──────────────────────────┘
```

## Features

- **Bilingual Tutoring** — Learn coding in Telugu (తెలుగు) or English
- **Code Review** — Get feedback on your code with suggestions
- **Problem Solving** — Step-by-step guidance for coding problems
- **RAG Pipeline** — Context-aware responses using Telugu programming corpus
- **Conversation Memory** — Persistent session context
- **Local LLM** — Fully offline, privacy-first using Ollama

## Quick Start

```bash
# 1. Install dependencies
pip install -r backend/requirements.txt

# 2. Start Ollama (ensure it's running)
ollama pull llama3.1:8b

# 3. Run Brihaspati
python -m backend.main
```

## API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Service health check |
| `/api/v1/chat` | POST | Chat with coding assistant |
| `/api/v1/teach` | POST | Request structured lesson |
| `/api/v1/code/review` | POST | Submit code for review |

## Tech Stack

- **Backend**: Python, FastAPI, Pydantic
- **AI**: Ollama (llama3.1, qwen2.5, codellama)
- **RAG**: ChromaDB, Sentence-Transformers
- **Memory**: JSON store / Redis (optional)
- **Container**: Docker, Docker Compose

## License

AGPL-3.0 — See [LICENSE](LICENSE).
