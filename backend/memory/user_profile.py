import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional
from backend.models.enums import Language

logger = logging.getLogger("brihaspati.memory")


class UserProfile:
    def __init__(self, store_path: str = "data/profiles"):
        self.store_path = Path(store_path)
        self.store_path.mkdir(parents=True, exist_ok=True)

    def get_or_create(self, user_id: str) -> dict:
        profile = self._load(user_id)
        if not profile:
            profile = self._create_default(user_id)
            self._save(user_id, profile)
        return profile

    def update_language(self, user_id: str, language: Language):
        profile = self.get_or_create(user_id)
        profile["preferred_language"] = language.value
        profile["updated_at"] = datetime.now().isoformat()
        self._save(user_id, profile)

    def add_topic(self, user_id: str, topic: str):
        profile = self.get_or_create(user_id)
        if topic not in profile["topics_covered"]:
            profile["topics_covered"].append(topic)
            profile["updated_at"] = datetime.now().isoformat()
        self._save(user_id, profile)

    def update_skill_level(self, user_id: str, level: str):
        profile = self.get_or_create(user_id)
        profile["skill_level"] = level
        profile["updated_at"] = datetime.now().isoformat()
        self._save(user_id, profile)

    def _create_default(self, user_id: str) -> dict:
        return {
            "user_id": user_id,
            "preferred_language": Language.ENGLISH.value,
            "skill_level": "beginner",
            "topics_covered": [],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }

    def _path(self, user_id: str) -> Path:
        return self.store_path / f"{user_id}.json"

    def _load(self, user_id: str) -> Optional[dict]:
        path = self._path(user_id)
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            return None

    def _save(self, user_id: str, profile: dict):
        path = self._path(user_id)
        path.write_text(json.dumps(profile, indent=2))
