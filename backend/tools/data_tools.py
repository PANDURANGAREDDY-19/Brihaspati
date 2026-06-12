import logging

logger = logging.getLogger("brihaspati.tools")


class DataTools:
    @staticmethod
    def validate_code_safety(code: str) -> tuple[bool, str]:
        dangerous_patterns = [
            ("os.system", "System command execution"),
            ("subprocess", "Subprocess execution"),
            ("eval(", "Code evaluation"),
            ("exec(", "Code execution"),
            ("__import__", "Dynamic import"),
            ("open(", "File operations (system files)"),
            ("shutil.rmtree", "File deletion"),
            ("import os", "OS module (full access)"),
        ]

        for pattern, description in dangerous_patterns:
            if pattern in code:
                return False, f"Unsafe code detected: {description}"

        return True, ""

    @staticmethod
    def truncate_response(text: str, max_length: int = 4000) -> str:
        if len(text) <= max_length:
            return text
        return text[: max_length - 3] + "..."

    @staticmethod
    def structure_lesson(topic: str, explanation: str, code_examples: list[str]) -> dict:
        return {
            "topic": topic,
            "explanation": explanation,
            "code_examples": code_examples,
            "exercises": DataTools._generate_exercise_prompts(topic),
        }

    @staticmethod
    def _generate_exercise_prompts(topic: str) -> list[str]:
        templates = [
            f"Write a program that demonstrates {topic}",
            f"Explain the difference between {topic} and related concepts",
            f"Create a real-world example using {topic}",
            f"Debug and fix an error in a {topic} implementation",
        ]
        return templates
