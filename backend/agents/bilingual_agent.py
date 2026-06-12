import logging
from typing import Optional
from backend.agents.base_agent import BaseAgent
from backend.services.ollama_service import OllamaService
from backend.services.translation_service import TranslationService
from backend.models.enums import Language

logger = logging.getLogger("brihaspati.agents")


class BilingualAgent(BaseAgent):
    def __init__(self, ollama_service: OllamaService, model: str = "llama3.1:8b"):
        super().__init__(
            name="bilingual_agent",
            ollama_service=ollama_service,
            model=model,
            temperature=0.2,
            system_prompt_path="configs/prompts/translator_system_prompt.txt",
        )
        self.translation_service = TranslationService()

    async def process(self, message: str, context: Optional[dict] = None) -> str:
        context = context or {}
        mode = context.get("mode", "translate")
        target_language = context.get("target_language", Language.TELUGU)

        if mode == "term":
            term = message.strip().lower()
            result = self.translation_service.explain_term(term)
            if result["found"]:
                return (
                    f"**{result['english']}** → {result['telugu']} "
                    f"({result['transliteration']})"
                )
            prompt = f"""Explain the programming term '{message}' in {target_language.value}.
Provide the Telugu translation if applicable, and explain the concept."""
            return await self.generate(prompt)

        if target_language == Language.TELUGU:
            prompt = f"""Translate the following to Telugu (తెలుగు) and explain:

{message}"""
        else:
            prompt = f"""Translate the following to English and explain:

{message}"""

        return await self.generate(prompt)
