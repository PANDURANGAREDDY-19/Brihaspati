import logging
from pathlib import Path
from typing import Optional
import chromadb
from chromadb.config import Settings as ChromaSettings
from backend.config import settings
from backend.services.ollama_service import OllamaService

logger = logging.getLogger("brihaspati.rag")


class VectorStore:
    def __init__(self, ollama_service: Optional[OllamaService] = None):
        self.ollama = ollama_service
        self.persist_dir = Path(settings.vector_store_path)
        self.persist_dir.mkdir(parents=True, exist_ok=True)

        self.client = chromadb.PersistentClient(
            path=str(self.persist_dir),
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        self.collection_name = "brihaspati_docs"
        self._ensure_collection()

    def _ensure_collection(self):
        try:
            self.collection = self.client.get_or_create_collection(
                name=self.collection_name,
                metadata={"hnsw:space": "cosine"},
            )
        except Exception as e:
            logger.error(f"Failed to create ChromaDB collection: {e}")
            raise

    async def add_documents(self, documents: list[dict]):
        if not documents:
            return

        texts = [doc["content"] for doc in documents]
        metadatas = [doc.get("metadata", {}) for doc in documents]
        ids = [
            f"doc_{i}_{metadatas[i].get('filename', 'unknown')}"
            for i in range(len(documents))
        ]

        if self.ollama:
            embeddings = []
            for text in texts:
                emb = await self.ollama.embed(text[:1000])
                embeddings.append(emb)
        else:
            embeddings = None

        self.collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids,
            embeddings=embeddings,
        )
        logger.info(f"Added {len(documents)} documents to vector store")

    async def search(self, query: str, top_k: int = 4) -> list[dict]:
        if self.ollama:
            query_embedding = await self.ollama.embed(query)
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
            )
        else:
            results = self.collection.query(
                query_texts=[query],
                n_results=top_k,
            )

        return self._format_results(results)

    def _format_results(self, results) -> list[dict]:
        formatted: list[dict] = []
        if not results or not results.get("documents"):
            return formatted

        for i in range(len(results["documents"][0])):
            formatted.append(
                {
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i]
                    if results.get("metadatas")
                    else {},
                    "distance": results["distances"][0][i]
                    if results.get("distances")
                    else 0,
                }
            )
        return formatted

    def is_ready(self) -> bool:
        try:
            self.collection.count()
            return True
        except Exception:
            return False

    def count(self) -> int:
        try:
            return self.collection.count()
        except Exception:
            return 0
