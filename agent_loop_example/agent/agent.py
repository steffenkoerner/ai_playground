
from .conversations import Conversation
from ..mcp.client import MCPClient
from .llm.client import LLMClient
from .models.llm_response import ChatRequest
import json

class Agent:
    def __init__(self, name, llm_client: LLMClient, mcp_client: MCPClient, model: str = "gpt-4o-mini"):
        self.name = name
        self.llm = llm_client
        self.model = model
        self.conversation = Conversation(f"You are a helpful assistant named {name}.")
        self.mcp = mcp_client

    def run(self, prompt):
        tools = self.mcp.list_tools()
        self.conversation.add_message("user", prompt)

        while True:

            request = ChatRequest(messages=self.conversation.messages, tools=tools, model=self.model)
            response = self.llm.chat_with_tools(request)

            if response.tool_calls:
                self.conversation.messages.append(response.message)
                for tool_call in response.tool_calls:
                    result = self.mcp.call_tool(tool_call)
                    self.conversation.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result),
                    })
            else:
                self.conversation.add_message("assistant", response.message.content)
                return response.message.content

