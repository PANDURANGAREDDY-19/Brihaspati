import json
from pathlib import Path

LOCALE_PATH = Path(__file__).resolve().parent.parent / "locales"

def load_locale(code: str = "en"):
    file = LOCALE_PATH / f"{code}.json"
    if not file.exists():
        file = LOCALE_PATH / "en.json"
    return json.loads(file.read_text(encoding='utf-8'))
