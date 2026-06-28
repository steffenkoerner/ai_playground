from pydantic import BaseModel
from openai import OpenAI
from ..llm.config import DEFAULT_MODEL
import json


class Conversation:
    """Manages a multi-turn chat session with an LLM."""

    def __init__(self, client: OpenAI, system_prompt: str):
        self.client = client
        self.messages: list[dict] = [{"role": "system", "content": system_prompt}]

    def add_message(self, role: str, content: str):
        """Add a message to the conversation history."""
        self.messages.append({"role": role, "content": content})

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
        self.messages.append({"role": "assistant", "content": parsed.model_dump_json()})
        return parsed
    
    def chat_with_tools(self, user_message: str, tools: list, model: str = DEFAULT_MODEL) -> str:

            response = self.client.chat.completions.create(
                model=model,
                messages=self.messages,
                tools=tools,
                tool_choice="auto",
            )

            return response.choices[0]


    def reset(self):
        """Clear history, keeping the system prompt."""
        self.messages = self.messages[:1]
