from functools import lru_cache
from backend.services.ollama_service import OllamaService
from backend.services.session_manager import SessionManager
from backend.services.code_executor import CodeExecutor
from backend.services.translation_service import TranslationService
from backend.memory.conversation_memory import ConversationMemory
from backend.rag.vector_store import VectorStore
from backend.rag.retrieval_pipeline import RetrievalPipeline
from backend.agents.router import AgentRouter


@lru_cache
def get_ollama_service() -> OllamaService:
    return OllamaService()


@lru_cache
def get_session_manager() -> SessionManager:
    return SessionManager()


@lru_cache
def get_code_executor() -> CodeExecutor:
    return CodeExecutor()


@lru_cache
def get_translation_service() -> TranslationService:
    return TranslationService()


@lru_cache
def get_conversation_memory() -> ConversationMemory:
    return ConversationMemory()


@lru_cache
def get_vector_store() -> VectorStore:
    return VectorStore(ollama_service=get_ollama_service())


@lru_cache
def get_retrieval_pipeline() -> RetrievalPipeline:
    return RetrievalPipeline(vector_store=get_vector_store())


@lru_cache
def get_agent_router() -> AgentRouter:
    return AgentRouter(
        ollama_service=get_ollama_service(),
        session_manager=get_session_manager(),
    )
