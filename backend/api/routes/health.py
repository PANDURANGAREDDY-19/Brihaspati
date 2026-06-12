from fastapi import APIRouter, Depends
from backend.models.schemas import HealthResponse
from backend.api.dependencies import get_ollama_service, get_vector_store
from backend.services.ollama_service import OllamaService
from backend.rag.vector_store import VectorStore
from backend.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def health_check(
    ollama: OllamaService = Depends(get_ollama_service),
    vector_store: VectorStore = Depends(get_vector_store),
):
    ollama_ok = await ollama.check_health()
    vector_ok = vector_store.is_ready()

    return HealthResponse(
        status="healthy" if ollama_ok else "degraded",
        version=settings.app_version,
        ollama_connected=ollama_ok,
        vector_store_ready=vector_ok,
    )
