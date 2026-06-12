import streamlit as st
import httpx

BACKEND_URL_KEY = "backend_url"
DEFAULT_BACKEND_URL = "http://localhost:8000"


def get_backend_url() -> str:
    return st.session_state.get(BACKEND_URL_KEY, DEFAULT_BACKEND_URL)


def set_backend_url(url: str):
    st.session_state[BACKEND_URL_KEY] = url.rstrip("/")


async def check_health() -> dict:
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            resp = await client.get(f"{get_backend_url()}/health")
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        return {"status": "unreachable", "error": str(e)}


async def chat(
    message: str, session_id: str = "streamlit", language: str = "en"
) -> dict:
    try:
        async with httpx.AsyncClient(timeout=180) as client:
            resp = await client.post(
                f"{get_backend_url()}/api/v1/chat",
                json={
                    "message": message,
                    "session_id": session_id,
                    "language": language,
                },
            )
            resp.raise_for_status()
            return resp.json()
    except httpx.HTTPStatusError as e:
        return {
            "response": f"Error: Backend returned {e.response.status_code}",
            "session_id": session_id,
            "language": language,
        }
    except Exception as e:
        return {
            "response": f"Error: {e}",
            "session_id": session_id,
            "language": language,
        }


async def review_code(code: str, language: str = "python") -> dict:
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                f"{get_backend_url()}/api/v1/code/review",
                json={"code": code, "language": language},
            )
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        return {
            "summary": f"Error: {e}",
            "issues": [],
            "suggestions": [],
            "corrected_code": None,
        }


async def teach(topic: str, language: str = "en", level: str = "beginner") -> dict:
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                f"{get_backend_url()}/api/v1/teach",
                json={"topic": topic, "language": language, "level": level},
            )
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        return {
            "topic": topic,
            "explanation": f"Error: {e}",
            "code_examples": [],
            "exercises": [],
            "language": language,
        }
