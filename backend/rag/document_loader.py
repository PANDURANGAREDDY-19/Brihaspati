import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger("brihaspati.rag")


class DocumentLoader:
    SUPPORTED_EXTENSIONS = {
        ".txt",
        ".md",
        ".py",
        ".js",
        ".json",
        ".yaml",
        ".yml",
        ".csv",
    }

    def __init__(self, datasets_path: str = "datasets"):
        self.datasets_path = Path(datasets_path)

    def load_all(self) -> list[dict]:
        documents: list[dict] = []
        for ext in self.SUPPORTED_EXTENSIONS:
            documents.extend(self._load_by_extension(ext))
        logger.info(f"Loaded {len(documents)} documents from datasets")
        return documents

    def load_from_directory(self, directory: str) -> list[dict]:
        dir_path = Path(directory)
        if not dir_path.exists():
            logger.warning(f"Directory {directory} does not exist")
            return []
        documents: list[dict] = []
        for file_path in dir_path.rglob("*"):
            if file_path.suffix in self.SUPPORTED_EXTENSIONS and file_path.is_file():
                doc = self._load_file(file_path)
                if doc:
                    documents.append(doc)
        return documents

    def _load_by_extension(self, extension: str) -> list[dict]:
        documents: list[dict] = []
        if not self.datasets_path.exists():
            return documents
        for file_path in self.datasets_path.rglob(f"*{extension}"):
            if file_path.is_file():
                doc = self._load_file(file_path)
                if doc:
                    documents.append(doc)
        return documents

    def _load_file(self, file_path: Path) -> Optional[dict]:
        try:
            content = file_path.read_text(encoding="utf-8")
            return {
                "content": content,
                "metadata": {
                    "source": str(file_path),
                    "filename": file_path.name,
                    "extension": file_path.suffix,
                    "category": file_path.parent.name,
                },
            }
        except Exception as e:
            logger.warning(f"Failed to load {file_path}: {e}")
            return None
