from openai import OpenAI
from ...llm.config import GITHUB_TOKEN, BASE_URL
from ..models.llm_response import LLMResponse


class LLMClient:
    def __init__(self,model: str = "gpt-4o-mini"):
        if not GITHUB_TOKEN:
            raise EnvironmentError("GITHUB_TOKEN environment variable is not set.")
        self.client = OpenAI(base_url=BASE_URL, api_key=GITHUB_TOKEN)
        self.model = model

    def chat_with_tools(self, messages: list[dict], tools: list, model: str) -> LLMResponse:

        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )
        llm_response = LLMResponse(
            finish_reason=response.choices[0].finish_reason,
            message=response.choices[0].message,
            tool_calls=response.choices[0].message.tool_calls if response.choices[0].finish_reason == "tool_calls" else [],
        )

        return llm_response
    
    # def chat(self, user_message: str, model: str = DEFAULT_MODEL) -> str:
    #     self.messages.append({"role": "user", "content": user_message})
    #     response = self.client.chat.completions.create(
    #         model=model,
    #         messages=self.messages,
    #     )
    #     reply = response.choices[0].message.content
    #     self.messages.append({"role": "assistant", "content": reply})
    #     return reply

    # def chat_structured(self, user_message: str, response_format: type[BaseModel], model: str = DEFAULT_MODEL) -> BaseModel:
    #     self.messages.append({"role": "user", "content": user_message})
    #     response = self.client.beta.chat.completions.parse(
    #         model=model,
    #         messages=self.messages,
    #         response_format=response_format,
    #     )
    #     parsed = response.choices[0].message.parsed
    #     self.messages.append({"role": "assistant", "content": parsed.model_dump_json()})
    #     return parsed
    


