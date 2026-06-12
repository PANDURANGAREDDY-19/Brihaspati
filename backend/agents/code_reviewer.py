import logging
from typing import Optional
from backend.agents.base_agent import BaseAgent
from backend.services.ollama_service import OllamaService

logger = logging.getLogger("brihaspati.agents")


class CodeReviewerAgent(BaseAgent):
    def __init__(self, ollama_service: OllamaService, model: str = "codellama:7b"):
        super().__init__(
            name="code_reviewer",
            ollama_service=ollama_service,
            model=model,
            temperature=0.1,
            system_prompt_path="configs/prompts/reviewer_system_prompt.txt",
        )

    async def process(self, message: str, context: Optional[dict] = None) -> str:
        context = context or {}
        language = context.get("language", "python")

        prompt = f"""Review the following {language} code.

```{language}
{message}
```

Provide:
1. A brief summary of what the code does
2. Issues found (categorized as critical/major/minor)
3. Specific suggestions for improvement
4. The corrected code if there are issues"""

        response = await self.generate(prompt)
        return response

    async def review_with_format(self, code: str, language: str = "python") -> dict:
        response = await self.process(code, {"language": language})
        return self._parse_review(response)

    def _parse_review(self, text: str) -> dict:
        return {
            "summary": text.split("\n")[0] if text else "",
            "full_review": text,
            "language": "python",
        }
