import pytest
from backend.services.code_executor import CodeExecutor


@pytest.mark.asyncio
async def test_code_executor_disabled():
    executor = CodeExecutor()
    result = await executor.execute("print('hello')")
    assert result["success"] is False
    assert "disabled" in result["error"]


@pytest.mark.asyncio
async def test_code_executor_unsupported_language():
    executor = CodeExecutor()
    result = await executor.execute("print('hello')", language="brainfuck")
    assert result["success"] is False
    assert "Unsupported" in result["error"]
