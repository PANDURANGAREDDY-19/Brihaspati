import pytest
from unittest.mock import MagicMock
from backend.agents.base_agent import BaseAgent


class MockAgent(BaseAgent):
    async def process(self, message, context=None):
        return f"Processed: {message}"


def test_agent_initialization():
    mock_ollama = MagicMock()
    agent = MockAgent(
        name="test_agent",
        ollama_service=mock_ollama,
        model="llama3.1:8b",
        temperature=0.5,
    )
    assert agent.name == "test_agent"
    assert agent.model == "llama3.1:8b"
    assert agent.temperature == 0.5


@pytest.mark.asyncio
async def test_agent_process():
    mock_ollama = MagicMock()
    agent = MockAgent(
        name="test_agent",
        ollama_service=mock_ollama,
    )
    result = await agent.process("hello")
    assert result == "Processed: hello"
