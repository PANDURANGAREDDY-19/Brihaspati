from pathlib import Path
import yaml
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Brihaspati"
    app_version: str = "1.0.0"
    debug: bool = False
    secret_key: str = "change-me"

    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4

    ollama_host: str = "http://localhost:11434"
    ollama_default_model: str = "qwen2.5:1.5b"
    ollama_embedding_model: str = "nomic-embed-text"
    ollama_timeout: int = 120

    vector_store_path: str = "./vector_db"
    chunk_size: int = 512
    chunk_overlap: int = 64
    top_k_retrieval: int = 4

    memory_type: str = "json"
    memory_ttl_hours: int = 24
    max_conversation_history: int = 50

    code_execution_enabled: bool = False
    code_execution_timeout: int = 10
    code_execution_max_output_length: int = 4096

    log_level: str = "INFO"
    log_file: str = "logs/brihaspati.log"

    model_config = {"env_prefix": "", "case_sensitive": False}

    @classmethod
    def from_yaml(cls, path: str = "configs/config.yaml") -> "Settings":
        config_path = Path(path)
        if not config_path.exists():
            return cls()
        with open(config_path) as f:
            data = yaml.safe_load(f)
        return cls(**cls._flatten(data))

    @staticmethod
    def _flatten(data: dict, parent_key: str = "") -> dict:
        items = {}
        for k, v in data.items():
            key = f"{parent_key}_{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(Settings._flatten(v, key))
            else:
                items[key] = v
        return items


settings = Settings()
