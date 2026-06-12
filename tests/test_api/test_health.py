import pytest
from httpx import AsyncClient, ASGITransport
from backend.main import app


@pytest.fixture
def client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_health_endpoint(client):
    async with client as ac:
        response = await ac.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "version" in data
        assert "ollama_connected" in data
        assert "vector_store_ready" in data


@pytest.mark.asyncio
async def test_root_endpoint(client):
    async with client as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data
