from enum import Enum


class Language(str, Enum):
    ENGLISH = "en"
    TELUGU = "te"


class AgentType(str, Enum):
    CODING_TUTOR = "coding_tutor"
    CODE_REVIEWER = "code_reviewer"
    PROBLEM_SOLVER = "problem_solver"
    BILINGUAL_AGENT = "bilingual_agent"
