import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional
from backend.services.ollama_service import OllamaService

logger = logging.getLogger("brihaspati.agents")


class BaseAgent(ABC):
    def __init__(
        self,
        name: str,
        ollama_service: OllamaService,
        model: str = "llama3.1:8b",
        temperature: float = 0.3,
        system_prompt_path: Optional[str] = None,
    ):
        self.name = name
        self.ollama = ollama_service
        self.model = model
        self.temperature = temperature
        self._system_prompt = self._load_prompt(system_prompt_path) if system_prompt_path else ""

    def _load_prompt(self, path: str) -> str:
        prompt_path = Path(path)
        if prompt_path.exists():
            return prompt_path.read_text().strip()
        logger.warning(f"System prompt not found at {path}")
        return ""

    @abstractmethod
    async def process(self, message: str, context: Optional[dict] = None) -> str:
        raise NotImplementedError

    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> str:
        return await self.ollama.generate(
            prompt=prompt,
            model=self.model,
            system_prompt=system_prompt or self._system_prompt,
            temperature=temperature or self.temperature,
        )
