from models.server import MCPServer

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

    def call_tool(self, name: str, arguments: dict):
        for server in self.server:
            if name in [t['function']['name'] for t in server.list_tools()]:
                return server.call_tool(name, arguments)
        return None