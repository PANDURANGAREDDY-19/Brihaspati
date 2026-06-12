import pytest


@pytest.mark.asyncio
async def test_ollama_service_initialization():
    from backend.services.ollama_service import OllamaService
    service = OllamaService()
    assert service.base_url == "http://localhost:11434"
    assert service.default_model == "llama3.1:8b"
    await service.close()
