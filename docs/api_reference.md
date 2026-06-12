# API Reference

## Base URL

```
http://localhost:8000
```

## Endpoints

### Health Check

```
GET /health
```

Returns service status.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "ollama_connected": true,
  "vector_store_ready": true
}
```

### Chat

```
POST /api/v1/chat
```

Send a message to the coding tutor.

**Request Body:**
```json
{
  "message": "Explain Python lists",
  "session_id": "user-session-1",
  "language": "en"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | string | Yes | User's message (1-4096 chars) |
| `session_id` | string | No | Session identifier (default: "default") |
| `language` | string | No | "en" or "te" (default: "en") |

**Response:**
```json
{
  "response": "Python lists are ordered collections...",
  "session_id": "user-session-1",
  "language": "en"
}
```

### Teach

```
POST /api/v1/teach
```

Request a structured lesson.

**Request Body:**
```json
{
  "topic": "functions",
  "language": "te",
  "level": "beginner"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `topic` | string | Yes | Topic to learn |
| `language` | string | No | "en" or "te" |
| `level` | string | No | "beginner", "intermediate", "advanced" |

### Code Review

```
POST /api/v1/code/review
```

Submit code for AI review.

**Request Body:**
```json
{
  "code": "def add(a, b):\n    return a + b",
  "language": "python"
}
```

### Code Execute

```
POST /api/v1/code/execute
```

Execute code in a sandbox (disabled by default).

## Error Handling

All endpoints return standard error responses:

```json
{
  "error": "Error message",
  "detail": "Detailed explanation"
}
```

Status codes:
- `200` Success
- `422` Validation error
- `500` Internal server error
- `503` Service unavailable (Ollama disconnected)
