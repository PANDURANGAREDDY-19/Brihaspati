import pytest
from httpx import AsyncClient, ASGITransport
from backend.main import app


@pytest.fixture
def client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_chat_endpoint_validation(client):
    async with client as ac:
        response = await ac.post(
            "/api/v1/chat",
            json={"message": "", "session_id": "test"},
        )
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_chat_endpoint_invalid_language(client):
    async with client as ac:
        response = await ac.post(
            "/api/v1/chat",
            json={
                "message": "Hello",
                "session_id": "test",
                "language": "invalid",
            },
        )
        assert response.status_code == 422
