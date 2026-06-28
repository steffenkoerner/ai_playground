from pydantic import BaseModel, ConfigDict
from typing import Any

class LLMResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    finish_reason: str
    message: Any
    tool_calls: list[Any]

