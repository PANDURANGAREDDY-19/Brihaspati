import json
from pathlib import Path

LOCALE_PATH = Path(__file__).resolve().parent.parent / "locales"


def load_locale(language_code: str):
    language_code = language_code.lower()
    locale_file = LOCALE_PATH / f"{language_code}.json"
    if not locale_file.exists():
        locale_file = LOCALE_PATH / "en.json"
    with open(locale_file, "r", encoding="utf-8") as file:
        return json.load(file)
