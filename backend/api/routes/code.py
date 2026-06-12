from fastapi import APIRouter, Depends, HTTPException
from backend.models.schemas import CodeReviewRequest, CodeReviewResponse
from backend.models.enums import AgentType
from backend.api.dependencies import get_agent_router, get_code_executor
from backend.agents.router import AgentRouter
from backend.services.code_executor import CodeExecutor

router = APIRouter(prefix="/api/v1/code", tags=["Code"])


@router.post("/review", response_model=CodeReviewResponse)
async def review_code(
    request: CodeReviewRequest,
    agent_router: AgentRouter = Depends(get_agent_router),
):
    try:
        response = await agent_router.route(
            message=request.code,
            agent_type=AgentType.CODE_REVIEWER,
            context={"language": request.language},
        )
        return CodeReviewResponse(
            summary=response,
            issues=[],
            suggestions=[],
            corrected_code=None,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/execute")
async def execute_code(
    request: CodeReviewRequest,
    code_executor: CodeExecutor = Depends(get_code_executor),
):
    try:
        result = await code_executor.execute(request.code, request.language)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
