from pydantic import BaseModel, Field
from typing import Optional
from backend.models.enums import Language


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4096)
    session_id: str = Field(default="default", max_length=128)
    language: Language = Language.ENGLISH


class ChatResponse(BaseModel):
    response: str
    session_id: str
    language: Language


class TeachRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=256)
    language: Language = Language.ENGLISH
    level: str = Field(default="beginner", pattern="^(beginner|intermediate|advanced)$")


class TeachResponse(BaseModel):
    topic: str
    explanation: str
    code_examples: list[str]
    exercises: list[str]
    language: Language


class CodeReviewRequest(BaseModel):
    code: str = Field(min_length=1, max_length=16384)
    language: str = Field(default="python", max_length=32)


class CodeReviewResponse(BaseModel):
    summary: str
    issues: list[dict]
    suggestions: list[str]
    corrected_code: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    version: str
    ollama_connected: bool
    vector_store_ready: bool


class SessionInfo(BaseModel):
    session_id: str
    message_count: int
    language: Language
    created_at: str
    last_active: str


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
