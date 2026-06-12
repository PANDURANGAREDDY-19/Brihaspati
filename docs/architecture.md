# Architecture

## System Overview

Brihaspati follows a modular layered architecture:

```
┌─────────────────────────────────────────────────┐
│                  Client Layer                    │
│  (Streamlit UI / VS Code Ext / Web UI / CLI)    │
└──────────────────┬──────────────────────────────┘
                   │ HTTP / WebSocket
┌──────────────────▼──────────────────────────────┐
│                 API Layer (FastAPI)              │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │
│  │   Chat   │ │  Teach   │ │  Code Review     │ │
│  └────┬─────┘ └────┬─────┘ └────────┬─────────┘ │
└───────┼────────────┼────────────────┼───────────┘
        │            │                │
┌───────▼────────────▼────────────────▼───────────┐
│               Agent Layer                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │
│  │  Coding  │ │   Code   │ │  Bilingual       │ │
│  │  Tutor   │ │ Reviewer │ │  Agent           │ │
│  └────┬─────┘ └────┬─────┘ └────────┬─────────┘ │
└───────┼────────────┼────────────────┼───────────┘
        │            │                │
┌───────▼────────────▼────────────────▼───────────┐
│              Service Layer                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │
│  │  Ollama  │ │   Code   │ │  Session         │ │
│  │ Service  │ │ Executor │ │  Manager         │ │
│  └──────────┘ └──────────┘ └──────────────────┘ │
└───────┬─────────────────────────────────────────┘
        │
┌───────▼─────────────────────────────────────────┐
│           RAG / Memory / Tools Layer            │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │
│  │ ChromaDB │ │  Memory  │ │     Tools        │ │
│  │   Store  │ │  Store   │ │                  │ │
│  └──────────┘ └──────────┘ └──────────────────┘ │
└─────────────────────────────────────────────────┘
```

## Data Flow

1. **Client sends request** → FastAPI validates via Pydantic schemas
2. **API routes** → Extract parameters, call appropriate agent
3. **Agent processes** → Builds prompt with context (memory + RAG)
4. **Ollama generates** → Local LLM inference
5. **Response returned** → Parsed, logged, stored in session
6. **Session updated** → Memory stores conversation turn

## Module Responsibilities

| Module | Responsibility |
|--------|---------------|
| `api/` | HTTP endpoints, validation, CORS |
| `agents/` | AI agent logic, prompt engineering |
| `services/` | External service integration (Ollama, execution) |
| `memory/` | Conversation and user profile persistence |
| `rag/` | Vector store, document retrieval, embeddings |
| `tools/` | Utility functions for code and data processing |
| `models/` | Pydantic schemas, enums, type definitions |
