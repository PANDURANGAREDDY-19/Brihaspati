import logging
from typing import Optional
from backend.agents import (
    CodingTutorAgent,
    CodeReviewerAgent,
    ProblemSolverAgent,
    BilingualAgent,
)
from backend.services.ollama_service import OllamaService
from backend.services.session_manager import SessionManager
from backend.models.enums import AgentType

logger = logging.getLogger("brihaspati.agents")


class AgentRouter:
    def __init__(
        self,
        ollama_service: OllamaService,
        session_manager: SessionManager,
    ):
        self.ollama = ollama_service
        self.session_manager = session_manager
        self._agents: dict[AgentType, object] = {}

    def get_agent(self, agent_type: AgentType):
        if agent_type not in self._agents:
            self._agents[agent_type] = self._create_agent(agent_type)
        return self._agents[agent_type]

    def _create_agent(self, agent_type: AgentType):
        if agent_type == AgentType.CODING_TUTOR:
            return CodingTutorAgent(self.ollama, self.session_manager)
        elif agent_type == AgentType.CODE_REVIEWER:
            return CodeReviewerAgent(self.ollama)
        elif agent_type == AgentType.PROBLEM_SOLVER:
            return ProblemSolverAgent(self.ollama)
        elif agent_type == AgentType.BILINGUAL_AGENT:
            return BilingualAgent(self.ollama)
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")

    async def route(
        self,
        message: str,
        agent_type: AgentType = AgentType.CODING_TUTOR,
        context: Optional[dict] = None,
    ) -> str:
        agent = self.get_agent(agent_type)
        response = await agent.process(message, context)
        return response
