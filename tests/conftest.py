import pytest
from backend.config import Settings


@pytest.fixture(autouse=True)
def test_settings():
    settings = Settings(
        ollama_host="http://localhost:11434",
        ollama_default_model="llama3.1:8b",
        debug=False,
    )
    return settings
