import logging

logger = logging.getLogger("brihaspati")


TELUGU_PROGRAMMING_TERMS = {
    "variable": "వేరియబుల్",
    "function": "ఫంక్షన్",
    "loop": "లూప్",
    "array": "అర్రే",
    "class": "క్లాస్",
    "object": "ఆబ్జెక్ట్",
    "method": "మెథడ్",
    "string": "స్ట్రింగ్",
    "integer": "పూర్ణాంకం",
    "float": "ఫ్లోట్",
    "boolean": "బూలియన్",
    "list": "జాబితా",
    "dictionary": "నిఘంటువు",
    "tuple": "టపుల్",
    "set": "సెట్",
    "condition": "షరతు",
    "exception": "మినహాయింపు",
    "module": "మాడ్యూల్",
    "package": "ప్యాకేజీ",
    "inheritance": "వారసత్వం",
    "polymorphism": "బహురూపత",
    "encapsulation": "ఎన్క్యాప్సులేషన్",
    "abstraction": "అబ్స్ట్రాక్షన్",
    "recursion": "పునరావృతం",
    "algorithm": "అల్గారిథమ్",
    "debug": "డీబగ్",
    "compile": "కంపైల్",
    "execute": "అమలు",
    "parameter": "పారామీటర్",
    "argument": "ఆర్గ్యుమెంట్",
    "return": "తిరిగి ఇవ్వు",
    "import": "దిగుమతి",
    "print": "ముద్రించు",
    "input": "ఇన్‌పుట్",
    "output": "అవుట్‌పుట్",
}


class TranslationService:
    @staticmethod
    def get_telugu_term(english_term: str) -> str:
        return TELUGU_PROGRAMMING_TERMS.get(english_term.lower(), english_term)

    @staticmethod
    def explain_term(term: str) -> dict:
        telugu = TELUGU_PROGRAMMING_TERMS.get(term.lower())
        if not telugu:
            return {
                "english": term,
                "telugu": None,
                "transliteration": None,
                "found": False,
            }
        return {
            "english": term,
            "telugu": telugu,
            "transliteration": TranslationService._transliterate(telugu),
            "found": True,
        }

    @staticmethod
    def _transliterate(telugu_text: str) -> str:
        mapping = {
            'అ': 'a', 'ఆ': 'ā', 'ఇ': 'i', 'ఈ': 'ī', 'ఉ': 'u', 'ఊ': 'ū',
            'ఋ': 'r̥', 'ఎ': 'e', 'ఏ': 'ē', 'ఐ': 'ai', 'ఒ': 'o', 'ఓ': 'ō',
            'ఔ': 'au', 'ం': 'm', 'ః': 'h',
            'క': 'ka', 'ఖ': 'kha', 'గ': 'ga', 'ఘ': 'gha', 'ఙ': 'ṅa',
            'చ': 'ca', 'ఛ': 'cha', 'జ': 'ja', 'ఝ': 'jha', 'ఞ': 'ña',
            'ట': 'ṭa', 'ఠ': 'ṭha', 'డ': 'ḍa', 'ఢ': 'ḍha', 'ణ': 'ṇa',
            'త': 'ta', 'థ': 'tha', 'ద': 'da', 'ధ': 'dha', 'న': 'na',
            'ప': 'pa', 'ఫ': 'pha', 'బ': 'ba', 'భ': 'bha', 'మ': 'ma',
            'య': 'ya', 'ర': 'ra', 'ల': 'la', 'వ': 'va', 'శ': 'śa',
            'ష': 'ṣa', 'స': 'sa', 'హ': 'ha', 'ళ': 'ḷa', 'క్ష': 'kṣa',
            '్': '', 'ి': 'i', 'ీ': 'ī', 'ు': 'u', 'ూ': 'ū',
            'ె': 'e', 'ే': 'ē', 'ై': 'ai', 'ొ': 'o', 'ో': 'ō',
            'ౌ': 'au',
        }
        result = []
        i = 0
        while i < len(telugu_text):
            char = telugu_text[i]
            result.append(mapping.get(char, char))
            i += 1
        return ''.join(result)
