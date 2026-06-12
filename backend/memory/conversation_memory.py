import json
import logging
from datetime import datetime
from pathlib import Path
from backend.config import settings

logger = logging.getLogger("brihaspati.memory")


class ConversationMemory:
    def __init__(self, store_path: str = "data/conversations"):
        self.store_path = Path(store_path)
        self.store_path.mkdir(parents=True, exist_ok=True)
        self.max_turns = settings.max_conversation_history

    def save_turn(self, session_id: str, user_message: str, assistant_response: str):
        path = self._path(session_id)
        turns = self._load(session_id)
        turns.append({
            "user": user_message,
            "assistant": assistant_response,
            "timestamp": datetime.now().isoformat(),
        })
        if len(turns) > self.max_turns:
            turns = turns[-self.max_turns:]
        path.write_text(json.dumps(turns, indent=2))

    def get_context(self, session_id: str, last_n: int = 5) -> list[dict]:
        turns = self._load(session_id)
        return turns[-last_n:]

    def get_formatted_history(self, session_id: str, last_n: int = 5) -> str:
        turns = self.get_context(session_id, last_n)
        if not turns:
            return ""
        lines = []
        for turn in turns:
            lines.append(f"User: {turn['user']}")
            lines.append(f"Assistant: {turn['assistant']}")
        return "\n".join(lines)

    def clear(self, session_id: str):
        path = self._path(session_id)
        if path.exists():
            path.unlink()

    def _path(self, session_id: str) -> Path:
        return self.store_path / f"{session_id}.json"

    def _load(self, session_id: str) -> list[dict]:
        path = self._path(session_id)
        if not path.exists():
            return []
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError) as e:
            logger.warning(f"Failed to load memory for {session_id}: {e}")
            return []
