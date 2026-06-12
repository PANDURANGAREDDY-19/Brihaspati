from backend.services.translation_service import TranslationService


def test_translation_known_term():
    result = TranslationService.explain_term("variable")
    assert result["found"] is True
    assert result["telugu"] == "వేరియబుల్"


def test_translation_unknown_term():
    result = TranslationService.explain_term("quantum_computing")
    assert result["found"] is False
    assert result["telugu"] is None


def test_telugu_term_lookup():
    term = TranslationService.get_telugu_term("loop")
    assert term == "లూప్"


def test_telugu_term_case_insensitive():
    term = TranslationService.get_telugu_term("Function")
    assert term == "ఫంక్షన్"
