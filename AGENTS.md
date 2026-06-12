# Brihaspati Agents

Brihaspati uses a multi-agent architecture for teaching coding bilingually.

## Agent Architecture

```
User Input
    │
    ▼
┌─────────────────────────────────────┐
│         Router Agent                │
│  (Routes queries to sub-agents)     │
└────┬──────┬──────┬──────┬───────────┘
     │      │      │      │
     ▼      ▼      ▼      ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────────┐
│Coding│ │ Code │ │Prob. │ │Bilingual │
│Tutor │ │Review│ │Solver│ │ Agent    │
└──┬───┘ └──┬───┘ └──┬───┘ └────┬─────┘
   │        │        │          │
   └────────┴────────┴──────────┘
                │
                ▼
         ┌─────────────┐
         │   Ollama    │
         │  (LLM)      │
         └─────────────┘
```

## Agent Descriptions

### 1. Coding Tutor Agent
- **Purpose**: Teaches programming concepts with explanations and examples
- **Capabilities**: Step-by-step tutorials, concept explanations, code walkthroughs
- **Prompt**: Located in `configs/prompts/tutor_system_prompt.txt`

### 2. Code Reviewer Agent
- **Purpose**: Reviews submitted code for correctness, style, and best practices
- **Capabilities**: Bug detection, style suggestions, performance optimization tips
- **Prompt**: Located in `configs/prompts/reviewer_system_prompt.txt`

### 3. Problem Solver Agent
- **Purpose**: Helps solve coding problems and assignments
- **Capabilities**: Problem breakdown, algorithm design, debugging assistance

### 4. Bilingual Agent
- **Purpose**: Translates between Telugu and English in coding contexts
- **Capabilities**: Code-switching, Telugu terminology mapping, bilingual explanations
- **Prompt**: Located in `configs/prompts/translator_system_prompt.txt`

## Agent Configuration

Agents are configured via `configs/config.yaml`. Each agent specifies:
- The Ollama model to use
- System prompt template
- Temperature and other LLM parameters
- Available tools

## Memory Integration

Each agent has access to:
- **Conversation Memory**: Last N turns of the current session
- **User Profile**: Preferred language, skill level, topics covered
- **RAG Context**: Retrieved documents from vector store

## Creating a New Agent

1. Create a new file in `backend/agents/`
2. Inherit from `BaseAgent` in `backend/agents/base_agent.py`
3. Register the agent in the router
4. Add system prompt in `configs/prompts/`

## Available Tools

Agents can use tools from `backend/tools/`:
- `CodeExecutor` - Run code snippets in sandboxed environment
- `DataAnalyzer` - Analyze datasets and provide insights
- `SearchDocs` - Search through documentation
- `FetchExample` - Fetch relevant code examples from the dataset
