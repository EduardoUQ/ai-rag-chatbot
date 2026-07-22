from app.models.conversation import Conversation
from app.models.message import Message


class ConversationManager:

    def __init__(self):
        self.conversations = {}

    def get_conversation(self, conversation_id: str) -> Conversation:

        if conversation_id not in self.conversations:

            self.conversations[conversation_id] = Conversation(
                conversation_id=conversation_id
            )

        return self.conversations[conversation_id]

    def add_user_message(self, conversation_id: str, content: str):

        conversation = self.get_conversation(conversation_id)

        conversation.messages.append(
            Message(
                role="user",
                content=content
            )
        )

    def add_assistant_message(self, conversation_id: str, content: str):

        conversation = self.get_conversation(conversation_id)

        conversation.messages.append(
            Message(
                role="assistant",
                content=content
            )
        )

