from pydantic import BaseModel, ConfigDict
from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from .config import DEFAULT_MODEL

@dataclass
class Message:
    role: str
    content: str | None
    tool_call_id: str | None = None
    tool_calls: list[Any] | None = None
    
class ChatResponse  (BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    finish_reason: str
    message: Message
    tool_calls: list[Any]

@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict


@dataclass
class ChatRequest:
    messages: list[Message]
    tools: list[dict] | None = None
    response_format: type | None = None
    model: str = DEFAULT_MODEL