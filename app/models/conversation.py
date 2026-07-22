from dataclasses import dataclass, field

from app.models.message import Message


@dataclass
class Conversation:

    conversation_id: str

    messages: list[Message] = field(default_factory=list)

    def to_openai_messages(self, system_prompt: str | None = None) -> list[dict[str, str]]:

        messages = []

        if system_prompt:

            messages.append({
                "role": "system",
                "content": system_prompt
            })

        messages.extend(
            {
                "role": message.role,
                "content": message.content
            }
            for message in self.messages
        )

        return messages

    