from fastapi import APIRouter

from app.models.requests import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)

chat_service = ChatService()


@router.post("/chat")
def chat(request: ChatRequest):

    return chat_service.chat(
        message=request.message,
        conversation_id=request.conversation_id
    )