from typing import Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        example="Pregunta del usuario"
    )

    conversation_id: Optional[str] = Field(
        default=None,
        example="Identificador de la conversación. Déjalo vacío para iniciar una nueva."
    )