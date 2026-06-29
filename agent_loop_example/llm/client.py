from openai import OpenAI
from .config import GITHUB_TOKEN, BASE_URL
from ..agent.models.llm_response import ChatResponse, ChatRequest, Message


class LLMClient:
    def __init__(self,model: str = "gpt-4o-mini"):
        if not GITHUB_TOKEN:
            raise EnvironmentError("GITHUB_TOKEN environment variable is not set.")
        self.client = OpenAI(base_url=BASE_URL, api_key=GITHUB_TOKEN)
        self.model = model

    def chat(self, request: ChatRequest) -> ChatResponse:

        response = self.client.chat.completions.create(
            model=request.model,
            messages=request.messages,
            tools=request.tools,
            tool_choice="auto",
        )
        llm_response = ChatResponse(
            finish_reason=response.choices[0].finish_reason,
            message=Message(
                role=response.choices[0].message.role,
                content=response.choices[0].message.content,
                tool_call_id=getattr(response.choices[0].message, "tool_call_id", None),
                tool_calls=response.choices[0].message.tool_calls or [],
            ),
            tool_calls=response.choices[0].message.tool_calls or [],
        )

        return llm_response


