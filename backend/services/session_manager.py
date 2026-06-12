import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from backend.config import settings
from backend.models.enums import Language

logger = logging.getLogger("brihaspati")


class SessionManager:
    def __init__(self):
        self.memory_type = settings.memory_type
        self.ttl = timedelta(hours=settings.memory_ttl_hours)
        self.max_history = settings.max_conversation_history
        self._store_path = Path("data/sessions")
        self._store_path.mkdir(parents=True, exist_ok=True)
        self._sessions: dict[str, dict] = {}
        self._load_all()

    def _session_path(self, session_id: str) -> Path:
        return self._store_path / f"{session_id}.json"

    def _load_all(self):
        if not self._store_path.exists():
            return
        for f in self._store_path.iterdir():
            if f.suffix == ".json":
                try:
                    data = json.loads(f.read_text())
                    self._sessions[f.stem] = data
                except (json.JSONDecodeError, OSError) as e:
                    logger.warning(f"Failed to load session {f.stem}: {e}")

    def _save(self, session_id: str):
        if session_id in self._sessions:
            path = self._session_path(session_id)
            path.write_text(json.dumps(self._sessions[session_id], indent=2))

    def get_or_create(self, session_id: str, language: Language = Language.ENGLISH) -> dict:
        if session_id not in self._sessions:
            self._sessions[session_id] = {
                "session_id": session_id,
                "language": language.value,
                "message_count": 0,
                "history": [],
                "created_at": datetime.now().isoformat(),
                "last_active": datetime.now().isoformat(),
            }
            self._save(session_id)
        return self._sessions[session_id]

    def add_message(self, session_id: str, role: str, content: str):
        session = self.get_or_create(session_id)
        session["history"].append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
        })
        session["message_count"] += 1
        session["last_active"] = datetime.now().isoformat()
        if len(session["history"]) > self.max_history:
            session["history"] = session["history"][-self.max_history:]
        self._save(session_id)

    def get_history(self, session_id: str, limit: int = 10) -> list[dict]:
        session = self.get_or_create(session_id)
        return session["history"][-limit:]

    def update_language(self, session_id: str, language: Language):
        session = self.get_or_create(session_id)
        session["language"] = language.value
        session["last_active"] = datetime.now().isoformat()
        self._save(session_id)

    def get_session_info(self, session_id: str) -> Optional[dict]:
        session = self.get_or_create(session_id)
        return {
            "session_id": session["session_id"],
            "message_count": session["message_count"],
            "language": session["language"],
            "created_at": session["created_at"],
            "last_active": session["last_active"],
        }

    def cleanup_expired(self):
        now = datetime.now()
        expired = []
        for sid, session in self._sessions.items():
            last_active = datetime.fromisoformat(session["last_active"])
            if now - last_active > self.ttl:
                expired.append(sid)
        for sid in expired:
            del self._sessions[sid]
            path = self._session_path(sid)
            if path.exists():
                path.unlink()
        if expired:
            logger.info(f"Cleaned up {len(expired)} expired sessions")
