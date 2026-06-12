# Brihaspati User Manual

Brihaspati is a Bilingual Coding Assistant that teaches programming in Telugu and English.

## Architecture Overview

```
User → API (FastAPI) → Agent System → Ollama (LLM)
                    → RAG Pipeline → Vector Store
                    → Memory Store
```

## API Endpoints

### Chat
```http
POST /api/v1/chat
```
Send a message to the coding tutor.

**Request:**
```json
{
  "message": "How do I write a for loop in Python?",
  "session_id": "session-123",
  "language": "en"
}
```

**Response:**
```json
{
  "response": "In Python, you write a for loop like this...",
  "session_id": "session-123",
  "language": "en"
}
```

### Teach
```http
POST /api/v1/teach
```
Request a structured lesson on a topic.

**Request:**
```json
{
  "topic": "variables",
  "language": "te"
}
```

**Response:**
```json
{
  "topic": "variables",
  "explanation": "వేరియబుల్స్ అంటే...",
  "code_examples": ["x = 5", "name = 'రాము'"],
  "exercises": ["ఒక వేరియబుల్‌ను సృష్టించండి"]
}
```

### Code Review
```http
POST /api/v1/code/review
```
Submit code for review.

**Request:**
```json
{
  "code": "def add(a,b): return a+b",
  "language": "python"
}
```

### Health
```http
GET /health
```
Returns service health status including Ollama connectivity.

## Usage Examples

### Start the server
```bash
python -m backend.main
```

### Send a coding question (English)
```python
import requests
response = requests.post(
    "http://localhost:8000/api/v1/chat",
    json={
        "message": "Explain recursion",
        "session_id": "user-001",
        "language": "en"
    }
)
print(response.json()["response"])
```

### Send a coding question (Telugu)
```python
response = requests.post(
    "http://localhost:8000/api/v1/chat",
    json={
        "message": "Python లో ఫంక్షన్ ఎలా రాయాలి?",
        "session_id": "user-001",
        "language": "te"
    }
)
print(response.json()["response"])
```

## Language Support

- `en` - English
- `te` - Telugu
- Both languages supported in all endpoints.

## Running with Docker

```bash
docker-compose -f docker/docker-compose.yml up
```

## Configuration

See `.env.example` for all configuration options.
