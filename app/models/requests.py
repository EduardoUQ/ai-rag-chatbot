from typing import Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        example="¿Quién es Eduardo?"
    )

    conversation_id: Optional[str] = Field(
        default=None,
        description="Conversation identifier. Leave empty to start a new conversation.",
        example=None
    )