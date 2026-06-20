from pydantic import BaseModel
from openai import OpenAI
from config import DEFAULT_MODEL


class Conversation:
    """Manages a multi-turn chat session with an LLM."""

    def __init__(self, client: OpenAI, system_prompt: str):
        self.client = client
        self.messages: list[dict] = [{"role": "system", "content": system_prompt}]

    def chat(self, user_message: str, model: str = DEFAULT_MODEL) -> str:
        self.messages.append({"role": "user", "content": user_message})
        response = self.client.chat.completions.create(
            model=model,
            messages=self.messages,
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def chat_structured(self, user_message: str, response_format: type[BaseModel], model: str = DEFAULT_MODEL) -> BaseModel:
        self.messages.append({"role": "user", "content": user_message})
        response = self.client.beta.chat.completions.parse(
            model=model,
            messages=self.messages,
            response_format=response_format,
        )
        parsed = response.choices[0].message.parsed
        self.messages.append({"role": "assistant", "content": str(parsed)})
        return parsed

    def reset(self):
        """Clear history, keeping the system prompt."""
        self.messages = self.messages[:1]
