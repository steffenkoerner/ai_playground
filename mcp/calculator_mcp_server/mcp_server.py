from models.server import MCPServer
from calculator_mcp_server.additor_tool import Additor
from calculator_mcp_server.subtractor_tool import Subtractor

class CalculatorMCPServer(MCPServer):
    def __init__(self):
        super().__init__()
        self.register(Additor())
        self.register(Subtractor())