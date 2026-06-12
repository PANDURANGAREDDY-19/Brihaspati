import json
import logging
import traceback
from typing import AsyncGenerator, Optional
import httpx
from backend.config import settings

logger = logging.getLogger("brihaspati.ollama")


class OllamaService:
    def __init__(self):
        self.base_url = settings.ollama_host.rstrip("/")
        self.default_model = settings.ollama_default_model
        self.timeout = settings.ollama_timeout

    async def check_health(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(self.timeout)) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                return response.status_code == 200
        except Exception as e:
            logger.warning(f"Ollama health check failed: {e}")
            return False

    async def list_models(self) -> list[dict]:
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(self.timeout)) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                response.raise_for_status()
                data = response.json()
                return data.get("models", [])
        except Exception as e:
            logger.error(f"Failed to list Ollama models: {e}")
            return []

    async def generate(
        self,
        prompt: str,
        model: Optional[str] = None,
        system_prompt: Optional[str] = None,
        temperature: float = 0.3,
        stream: bool = False,
    ) -> str:
        payload = {
            "model": model or self.default_model,
            "prompt": prompt,
            "temperature": temperature,
            "stream": stream,
        }
        if system_prompt:
            payload["system"] = system_prompt

        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(self.timeout)) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json=payload,
                )
                response.raise_for_status()

                if stream:
                    full_response = ""
                    async for line in response.aiter_lines():
                        if line:
                            try:
                                chunk = json.loads(line)
                                full_response += chunk.get("response", "")
                                if chunk.get("done"):
                                    break
                            except json.JSONDecodeError:
                                continue
                    return full_response

                data = response.json()
                return data.get("response", "")

        except Exception as e:
            logger.error(f"Ollama generate failed: {e}\n{traceback.format_exc()}")
            raise RuntimeError(f"Failed to generate response from Ollama: {e}")

    async def generate_stream(
        self,
        prompt: str,
        model: Optional[str] = None,
        system_prompt: Optional[str] = None,
        temperature: float = 0.3,
    ) -> AsyncGenerator[str, None]:
        payload = {
            "model": model or self.default_model,
            "prompt": prompt,
            "temperature": temperature,
            "stream": True,
        }
        if system_prompt:
            payload["system"] = system_prompt

        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(self.timeout)) as client:
                async with client.stream(
                    "POST",
                    f"{self.base_url}/api/generate",
                    json=payload,
                ) as response:
                    response.raise_for_status()
                    async for line in response.aiter_lines():
                        if line:
                            try:
                                chunk = json.loads(line)
                                content = chunk.get("response", "")
                                if content:
                                    yield content
                                if chunk.get("done"):
                                    break
                            except json.JSONDecodeError:
                                continue
        except Exception as e:
            logger.error(f"Ollama stream failed: {e}\n{traceback.format_exc()}")
            raise RuntimeError(f"Failed to stream from Ollama: {e}")

    async def embed(self, text: str) -> list[float]:
        payload = {
            "model": settings.ollama_embedding_model,
            "prompt": text,
        }
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(self.timeout)) as client:
                response = await client.post(
                    f"{self.base_url}/api/embeddings",
                    json=payload,
                )
                response.raise_for_status()
                data = response.json()
                return data.get("embedding", [])
        except Exception as e:
            logger.error(f"Ollama embedding failed: {e}\n{traceback.format_exc()}")
            raise RuntimeError(f"Failed to get embeddings: {e}")

    async def close(self):
        pass
