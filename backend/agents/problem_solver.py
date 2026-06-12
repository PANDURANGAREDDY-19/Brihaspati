import logging
from typing import Optional
from backend.agents.base_agent import BaseAgent
from backend.services.ollama_service import OllamaService

logger = logging.getLogger("brihaspati.agents")


class ProblemSolverAgent(BaseAgent):
    def __init__(self, ollama_service: OllamaService, model: str = "llama3.1:8b"):
        super().__init__(
            name="problem_solver",
            ollama_service=ollama_service,
            model=model,
            temperature=0.4,
            system_prompt_path="configs/prompts/solver_system_prompt.txt",
        )
        self._load_default_prompt()

    def _load_default_prompt(self):
        self._system_prompt = """You are Brihaspati's problem-solving agent. Help users solve coding problems step by step.

Rules:
1. First understand the problem fully
2. Break it down into smaller sub-problems
3. Explain your reasoning for each step
4. Provide the complete solution at the end
5. Suggest test cases to verify the solution
6. Point out alternative approaches

Always teach, don't just give the answer."""

    async def process(self, message: str, context: Optional[dict] = None) -> str:
        prompt = f"""Problem: {message}

Solve this step by step:
1. Problem understanding
2. Approach
3. Algorithm
4. Code solution
5. Test cases
6. Alternative approaches"""
        return await self.generate(prompt)
