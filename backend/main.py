import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.config import settings
from backend.api.middlewares.cors import setup_cors
from backend.api.routes.health import router as health_router
from backend.api.routes.chat import router as chat_router
from backend.api.routes.teach import router as teach_router
from backend.api.routes.code import router as code_router
from backend.api.dependencies import get_ollama_service

logger = logging.getLogger("brihaspati")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    ollama = get_ollama_service()
    ollama_ok = await ollama.check_health()
    if ollama_ok:
        logger.info("Ollama is connected and healthy")
    else:
        logger.warning("Ollama is not available. Some features may be limited.")
    yield
    await ollama.close()
    logger.info("Brihaspati shutdown complete")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Bilingual Coding Assistant — Teach programming in Telugu and English",
    lifespan=lifespan,
)

setup_cors(app)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(teach_router)
app.include_router(code_router)


@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "docs": "/docs",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
