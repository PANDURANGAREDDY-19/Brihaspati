from fastapi import APIRouter, Depends, HTTPException
from backend.models.schemas import TeachRequest, TeachResponse
from backend.models.enums import AgentType
from backend.api.dependencies import get_agent_router
from backend.agents.router import AgentRouter

router = APIRouter(prefix="/api/v1", tags=["Teaching"])


@router.post("/teach", response_model=TeachResponse)
async def teach(
    request: TeachRequest,
    agent_router: AgentRouter = Depends(get_agent_router),
):
    try:
        prompt = (
            f"Teach me about '{request.topic}' at {request.level} level. "
            f"Provide:\n"
            f"1. A clear explanation\n"
            f"2. Code examples\n"
            f"3. Practice exercises\n"
            f"4. Common mistakes to avoid"
        )

        response = await agent_router.route(
            message=prompt,
            agent_type=AgentType.CODING_TUTOR,
            context={"language": request.language},
        )

        return TeachResponse(
            topic=request.topic,
            explanation=response,
            code_examples=[""],
            exercises=[""],
            language=request.language,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
