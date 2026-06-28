
from .conversations import Conversation
from ..mcp.client import MCPClient
from ..llm.client import LLMClient
from ..mcp.servers.calculator_mcp_server.mcp_server import CalculatorMCPServer
from ..mcp.servers.weather_mcp_server.mcp_server import WeatherMCPServer
import json

class Agent:
    def __init__(self, name, llm_client: LLMClient, mcp_client: MCPClient):
        self.name = name
        llm = llm_client
        self.conversation = Conversation(llm.client, f"You are a helpful assistant named {name}.")
        self.mcp = mcp_client


    def run(self, prompt):
        tools = self.mcp.list_tools()
        self.conversation.add_message("user", prompt)

        while True:
            response = self.conversation.chat_with_tools(prompt, tools, model=self.model)

            if response.finish_reason == "tool_calls":
                self.conversation.messages.append(response.message)
                for tool_call in response.message.tool_calls:
                    arguments = json.loads(tool_call.function.arguments)
                    result = self.mcp.call_tool(tool_call.function.name, arguments)
                    self.conversation.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result),
                    })
            else:
                reply = response.message.content
                self.conversation.add_message("assistant", reply)
                return reply
