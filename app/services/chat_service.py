from core.config import OPENAI_API_KEY, OPENAI_MODEL
from openai import OpenAI
from app.services.conversation_manager import ConversationManager
from app.services.rag_service import RAGService
from app.prompts.rag_prompt import RAG_PROMPT
from uuid import uuid4

class ChatService:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.conversation_manager = ConversationManager()
        self.rag_service = RAGService()

    def chat(self, message: str, conversation_id: str | None = None) -> dict:

        # Si es una conversación nueva
        if conversation_id is None:
            conversation_id = str(uuid4())

        # Guardar mensaje del usuario
        self.conversation_manager.add_user_message(
            conversation_id,
            message
        )

        # Recuperar contexto relevante usando RAG
        context = self.rag_service.retrieve_context(message)

        system_prompt = RAG_PROMPT.format(context=context)

        # Obtener la conversación completa
        conversation = self.conversation_manager.get_conversation(
            conversation_id
        )

        # Preparar mensajes para enviar a OpenAI
        messages = conversation.to_openai_messages(system_prompt=system_prompt)
        

        # Enviar historial a OpenAI
        response = self.client.responses.create(
            model=OPENAI_MODEL,
            input=messages
        )

        assistant_message = response.output_text

        # Guardar respuesta
        self.conversation_manager.add_assistant_message(
            conversation_id,
            assistant_message
        )

        return {
            "conversation_id": conversation_id,
            "response": assistant_message
        }