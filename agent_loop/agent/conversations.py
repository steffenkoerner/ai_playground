
class Conversation:
    """Manages a multi-turn chat session with an LLM."""

    def __init__(self, system_prompt: str):

        self.messages: list[dict] = [{"role": "system", "content": system_prompt}]

    def add_message(self, role: str, content: str):
        """Add a message to the conversation history."""
        self.messages.append({"role": role, "content": content})

    def get_messages(self) -> list[dict]:
        """Get the current conversation history."""
        return self.messages

    def reset(self):
        """Clear history, keeping the system prompt."""
        self.messages = self.messages[:1]
