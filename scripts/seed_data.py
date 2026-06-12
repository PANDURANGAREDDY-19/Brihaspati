#!/usr/bin/env python3
"""Seed the vector store with Telugu programming dataset examples."""

import asyncio
import logging
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.rag.vector_store import VectorStore
from backend.rag.document_loader import DocumentLoader
from backend.services.ollama_service import OllamaService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info("Starting data seeding...")

    ollama = OllamaService()
    vector_store = VectorStore(ollama_service=ollama)

    loader = DocumentLoader(datasets_path="datasets")
    documents = loader.load_all()

    if not documents:
        logger.warning("No documents found in datasets/. Adding sample documents...")
        documents = [
            {
                "content": "Python variables: Variables store data values. x = 5 assigns 5 to x.",
                "metadata": {"source": "builtin", "filename": "python_basics.txt", "category": "python"},
            },
            {
                "content": "For loop: for i in range(5): print(i) iterates 5 times.",
                "metadata": {"source": "builtin", "filename": "loops.txt", "category": "python"},
            },
            {
                "content": "తెలుగులో వేరియబుల్: వేరియబుల్ అంటే డేటాను నిల్వ చేసే కంటైనర్. x = 5 అని రాస్తే x లో 5 నిల్వ అవుతుంది.",
                "metadata": {"source": "builtin", "filename": "telugu_basics.txt", "category": "telugu_programming"},
            },
        ]

    await vector_store.add_documents(documents)
    count = vector_store.count()
    logger.info(f"Seeding complete! Vector store has {count} documents.")

    await ollama.close()


if __name__ == "__main__":
    asyncio.run(main())
