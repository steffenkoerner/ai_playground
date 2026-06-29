from agent_loop.agent.models.llm_response import ToolCall
import json

class MCPClient:
    def __init__(self):
        self.server = []

    def register(self, mcp_server):
        self.server.append(mcp_server)

    def list_tools(self):
        tools = []
        for server in self.server:
            tools.extend(server.list_tools())
        return tools

    def call_tool(self, tool_call: ToolCall):
        name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        for server in self.server:
            if name in server.tools:
                return server.call_tool(name, arguments)
        raise ValueError(f"Tool '{name}' not found")
