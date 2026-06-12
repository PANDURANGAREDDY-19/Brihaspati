from fastapi import APIRouter, Depends, HTTPException
from backend.models.schemas import ChatRequest, ChatResponse
from backend.models.enums import AgentType
from backend.api.dependencies import get_agent_router, get_session_manager
from backend.agents.router import AgentRouter
from backend.services.session_manager import SessionManager

router = APIRouter(prefix="/api/v1", tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    agent_router: AgentRouter = Depends(get_agent_router),
    session_manager: SessionManager = Depends(get_session_manager),
):
    try:
        context = {
            "session_id": request.session_id,
            "language": request.language,
        }

        response = await agent_router.route(
            message=request.message,
            agent_type=AgentType.CODING_TUTOR,
            context=context,
        )

        session_manager.add_message(request.session_id, "user", request.message)
        session_manager.add_message(request.session_id, "assistant", response)

        return ChatResponse(
            response=response,
            session_id=request.session_id,
            language=request.language,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
