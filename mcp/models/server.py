from models.tools import Tool

class MCPServer:
    def __init__(self):
        self.tools = {}

    def register(self, tool: Tool):
        self.tools[tool.name] = tool

    def list_tools(self):
        return [t.schema() for t in self.tools.values()]

    def call_tool(self, name: str, arguments: dict):
        return self.tools[name].execute(arguments)