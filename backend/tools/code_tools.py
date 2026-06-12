import logging

logger = logging.getLogger("brihaspati.tools")


class CodeTools:
    @staticmethod
    def extract_code_blocks(text: str) -> list[dict]:
        blocks = []
        lines = text.split("\n")
        in_block = False
        current_block = ""
        current_language = ""

        for line in lines:
            if line.startswith("```"):
                if in_block:
                    blocks.append({
                        "language": current_language,
                        "code": current_block.strip(),
                    })
                    current_block = ""
                    in_block = False
                else:
                    in_block = True
                    current_language = line[3:].strip()
            elif in_block:
                current_block += line + "\n"

        return blocks

    @staticmethod
    def detect_language(code: str) -> str:
        heuristics = {
            "python": ["def ", "import ", "class ", "print(", "if __name__", "lambda"],
            "javascript": ["function ", "const ", "let ", "var ", "=>", "console.log"],
            "java": ["public class", "private ", "System.out", "static void"],
            "cpp": ["#include", "int main", "std::", "cout <<"],
            "html": ["<!DOCTYPE", "<html", "<div", "<body"],
        }
        for lang, patterns in heuristics.items():
            for pattern in patterns:
                if pattern in code:
                    return lang
        return "python"

    @staticmethod
    def format_code_response(code: str, language: str = "python") -> str:
        return f"```{language}\n{code}\n```"
