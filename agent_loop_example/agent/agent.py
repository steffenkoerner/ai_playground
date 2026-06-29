
from .conversations import Conversation
from ..mcp.client import MCPClient
from ..llm.client import LLMClient
from .models.llm_response import ChatRequest, Message
class Agent:
    def __init__(self, name, llm_client: LLMClient, mcp_client: MCPClient, model: str = "gpt-4o-mini"):
        self.name = name
        self.llm = llm_client
        self.model = model
        self.conversation = Conversation(f"You are a helpful assistant named {name}.")
        self.mcp = mcp_client

    def run(self, prompt):
        tools = self.mcp.list_tools()
        self.conversation.add_message(Message(role="user", content=prompt))

        while True:

            request = ChatRequest(messages=self.conversation.get_messages(), tools=tools, model=self.model)
            response = self.llm.chat(request)

            if response.finish_reason == "tool_calls":
                self.conversation.add_message(response.message)
                for tool_call in response.message.tool_calls:
                    result = self.mcp.execute(tool_call)
                    self.conversation.add_message(Message(role="tool", content=str(result), tool_call_id=tool_call.id))
            else:
                self.conversation.add_message(Message(role="assistant", content=response.message.content))
                return response.message.content

