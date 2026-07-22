from typing import Optional
from pydantic import BaseModel, ConfigDict
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "¿Quién es Eduardo?"
            }
        }
    )