from .models.llm_response import Message
class Conversation:
    """Manages a multi-turn chat session with an LLM."""

    def __init__(self, system_prompt: str):

        self.messages: list[dict] = [{"role": "system", "content": system_prompt}]

    def add_message(self, message: Message):
        """Add a message to the conversation history."""
        if message.role == "tool":
            self.messages.append({"role": message.role, "content": message.content, "tool_call_id": message.tool_call_id})
        elif message.tool_calls:
            self.messages.append({"role": message.role, "content": message.content, "tool_calls": message.tool_calls})
        else:
            self.messages.append({"role": message.role, "content": message.content})

    def get_messages(self) -> list[dict]:
        """Get the current conversation history."""
        return self.messages

    def reset(self):
        """Clear history, keeping the system prompt."""
        self.messages = self.messages[:1]
