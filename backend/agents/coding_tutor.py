import logging
from typing import Optional
from backend.agents.base_agent import BaseAgent
from backend.services.ollama_service import OllamaService
from backend.services.session_manager import SessionManager
from backend.models.enums import Language
from backend.config import settings

logger = logging.getLogger("brihaspati.agents")


LANGUAGE_PROMPTS = {
    Language.ENGLISH: {
        "instruction": "IMPORTANT: You MUST respond entirely in English.",
        "reminder": "Remember: Your entire response must be in English only.",
    },
    Language.TELUGU: {
        "instruction": (
            "చివరి సూచన: మీరు తెలుగులో మాత్రమే సమాధానం ఇవ్వాలి.\n"
            "కోడ్ ఉదాహరణలు మాత్రమే ఆంగ్లంలో ఉండవచ్చు.\n"
            "మొదట తెలుగులో వివరించండి, తరువాత కోడ్ చూపించండి.\n"
            "ఉదాహరణ:\n"
            "ప్ర: What is a variable?\n"
            "తెలుగు సమాధానం: వేరియబుల్ అనేది డేటాను నిల్వ చేయడానికి ఉపయోగించే ఒక కంటైనర్. ఇది కంప్యూటర్ మెమరీలో ఒక స్థానాన్ని సూచిస్తుంది."
        ),
        "reminder": "గుర్తుంచుకోండి: మీరు తెలుగులో మాత్రమే సమాధానం రాయాలి. ఇంగ్లీష్ పదాలు ఉపయోగించకండి.",
    },
}


class CodingTutorAgent(BaseAgent):
    def __init__(
        self,
        ollama_service: OllamaService,
        session_manager: SessionManager,
        model: str = settings.ollama_default_model,
    ):
        super().__init__(
            name="coding_tutor",
            ollama_service=ollama_service,
            model=model,
            temperature=0.3,
            system_prompt_path="configs/prompts/tutor_system_prompt.txt",
        )
        self.session_manager = session_manager

    async def process(self, message: str, context: Optional[dict] = None) -> str:
        context = context or {}
        language = context.get("language", Language.ENGLISH)
        session_id = context.get("session_id", "default")

        history = self.session_manager.get_history(session_id, limit=6)
        history_text = self._format_history(history)

        lang = LANGUAGE_PROMPTS.get(language, LANGUAGE_PROMPTS[Language.ENGLISH])

        prompt = f"""{lang['instruction']}

Previous conversation:
{history_text}

Student's question: {message}

{lang['reminder']}

Provide a clear, educational explanation with code examples where appropriate."""

        response = await self.generate(prompt)
        return response

    def _format_history(self, history: list[dict]) -> str:
        if not history:
            return "(No prior conversation)"
        lines = []
        for entry in history:
            role = entry.get("role", "user")
            content = entry.get("content", "")
            # Truncate to avoid token overflow
            if len(content) > 500:
                content = content[:500] + "..."
            lines.append(f"{role}: {content}")
        return "\n".join(lines[-6:])
