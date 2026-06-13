import json
import re
import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from backend.api.dependencies import get_ollama_service
from backend.services.ollama_service import OllamaService

logger = logging.getLogger("brihaspati.quiz")

router = APIRouter(prefix="/api/v1/quiz", tags=["Quiz"])


class QuizQuestion(BaseModel):
    question: str
    options: list[str]
    answer: str
    explanation: str


class QuizGenerateRequest(BaseModel):
    language: str = Field(default="Python", max_length=32)
    topic: str = Field(default="Lists", max_length=64)
    difficulty: str = Field(default="Easy", pattern="^(Easy|Medium|Hard)$")
    num_questions: int = Field(default=5, ge=5, le=20)
    model: Optional[str] = None


class QuizGenerateResponse(BaseModel):
    questions: list[QuizQuestion]
    language: str
    topic: str
    difficulty: str


SYSTEM_PROMPT = """You are a programming quiz generator. Output ONLY valid JSON.
The root must be a JSON object (not an array) with this exact structure:
{
  "questions": [
    {
      "question": "Question text here?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": "The exact correct option text (no extra quotes)",
      "explanation": "Brief explanation"
    }
  ]
}
Rules:
- Generate exactly the requested number of questions
- Questions must about the given programming language, topic, and difficulty level
- Each question must have exactly 4 options
- The answer string must match one of the options EXACTLY (same text, no extra quotes)
- Questions must be unique and non-trivial
- NO markdown, NO code fences, NO extra text before or after the JSON"""


def _normalize(text: str) -> str:
    return text.strip().strip("'\"\u2018\u2019\u201c\u201d")


def _extract_json(raw: str) -> dict:
    raw = raw.strip()
    json_match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not json_match:
        raise ValueError("No JSON object found in LLM response")
    cleaned = json_match.group(0)
    return json.loads(cleaned)


def _parse_questions(raw: str) -> list[dict]:
    data = _extract_json(raw)
    questions = data.get("questions", [])
    if not questions:
        questions = data.get("quiz", [])
    if not questions:
        for val in data.values():
            if (
                isinstance(val, list)
                and len(val) > 0
                and isinstance(val[0], dict)
                and "question" in val[0]
            ):
                questions = val
                break
    if not questions:
        raise ValueError("No questions array found in LLM response")
    return questions


def _validate_question(q: dict) -> dict | None:
    if not isinstance(q, dict):
        return None
    question = q.get("question")
    options = q.get("options")
    answer = q.get("answer")
    explanation = q.get("explanation") or q.get("explain", "")
    if not question or not options or not answer:
        return None
    if not isinstance(options, list) or len(options) != 4:
        return None
    q["explanation"] = explanation
    q["options"] = [str(o) for o in options]
    q["answer"] = str(answer)
    q["question"] = str(question)

    normalized_answer = _normalize(q["answer"])
    normalized_options = [_normalize(o) for o in q["options"]]
    if normalized_answer not in normalized_options:
        logger.warning(f"Answer '{q['answer']}' not in options after normalization")
        return None
    idx = normalized_options.index(normalized_answer)
    q["answer"] = q["options"][idx]
    return q


@router.post("/generate", response_model=QuizGenerateResponse)
async def generate_quiz(
    request: QuizGenerateRequest,
    ollama: OllamaService = Depends(get_ollama_service),
):
    prompt = (
        f"Generate {request.num_questions} {request.difficulty} difficulty quiz questions "
        f"about {request.topic} in {request.language} programming language. "
        f"Each question must have exactly 4 options with one correct answer. "
        f"Return a JSON object with a 'questions' array."
    )

    for attempt in range(3):
        try:
            raw = await ollama.generate(
                prompt=prompt,
                model=request.model,
                system_prompt=SYSTEM_PROMPT,
                temperature=0.7,
            )
            questions_data = _parse_questions(raw)

            validated = []
            for q in questions_data:
                vq = _validate_question(q)
                if vq:
                    validated.append(QuizQuestion(**vq))

            if len(validated) >= request.num_questions:
                validated = validated[: request.num_questions]
                return QuizGenerateResponse(
                    questions=validated,
                    language=request.language,
                    topic=request.topic,
                    difficulty=request.difficulty,
                )

            logger.warning(
                f"Attempt {attempt + 1}: got {len(validated)}/{request.num_questions} valid questions"
            )

        except (json.JSONDecodeError, ValueError, KeyError) as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")

    raise HTTPException(
        status_code=500,
        detail="Failed to generate valid quiz questions. Please try again.",
    )
