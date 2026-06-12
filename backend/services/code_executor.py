import subprocess
import logging
import tempfile
from pathlib import Path
from backend.config import settings

logger = logging.getLogger("brihaspati")


class CodeExecutor:
    LANGUAGE_CONFIG = {
        "python": {
            "extension": ".py",
            "command": ["python3"],
        },
        "javascript": {
            "extension": ".js",
            "command": ["node"],
        },
        "cpp": {
            "extension": ".cpp",
            "command": ["g++", "-o", "{exec}", "{file}", "&&", "{exec}"],
        },
        "java": {
            "extension": ".java",
            "command": ["javac", "{file}", "&&", "java", "{class}"],
        },
    }

    def __init__(self):
        self.enabled = settings.code_execution_enabled
        self.timeout = settings.code_execution_timeout
        self.max_output = settings.code_execution_max_output_length

    async def execute(self, code: str, language: str = "python") -> dict:
        lang_config = self.LANGUAGE_CONFIG.get(language.lower())
        if not lang_config:
            return {
                "success": False,
                "output": "",
                "error": f"Unsupported language: {language}",
            }

        if not self.enabled:
            return {
                "success": False,
                "output": "",
                "error": "Code execution is disabled",
            }

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / f"script{lang_config['extension']}"
            file_path.write_text(code)

            try:
                result = subprocess.run(
                    ["python3", str(file_path)],
                    capture_output=True,
                    text=True,
                    timeout=self.timeout,
                    cwd=tmpdir,
                )
                output = result.stdout[-self.max_output:] if result.stdout else ""
                error = result.stderr[-self.max_output:] if result.stderr else ""
                return {
                    "success": result.returncode == 0,
                    "output": output,
                    "error": error,
                }
            except subprocess.TimeoutExpired:
                return {
                    "success": False,
                    "output": "",
                    "error": f"Execution timed out after {self.timeout}s",
                }
            except Exception as e:
                return {
                    "success": False,
                    "output": "",
                    "error": str(e),
                }
