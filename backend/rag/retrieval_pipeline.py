import logging
from typing import Optional
from backend.rag.vector_store import VectorStore
from backend.config import settings

logger = logging.getLogger("brihaspati.rag")


class RetrievalPipeline:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store
        self.top_k = settings.top_k_retrieval

    async def retrieve(self, query: str, top_k: Optional[int] = None) -> list[dict]:
        k = top_k or self.top_k
        results = await self.vector_store.search(query, top_k=k)
        return results

    def format_context(self, results: list[dict], max_chars: int = 2000) -> str:
        if not results:
            return ""

        sections = []
        total = 0
        for r in results:
            content = r["content"][:600]
            if total + len(content) > max_chars:
                break
            source = r["metadata"].get("filename", "unknown")
            sections.append(f"[Source: {source}]\n{content}")
            total += len(content)

        return "\n\n---\n\n".join(sections)

    async def augment_prompt(self, query: str, prompt: str) -> str:
        results = await self.retrieve(query)
        context = self.format_context(results)
        if not context:
            return prompt

        return f"""Use the following reference material to answer the question.

Reference Material:
{context}

Question/Task: {prompt}

Answer based on the reference material where applicable. If the reference
material doesn't contain relevant information, answer based on your knowledge."""
