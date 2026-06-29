from ...protocols.server import MCPServer
from .additor_tool import Additor
from .subtractor_tool import Subtractor

class CalculatorMCPServer(MCPServer):
    def __init__(self):
        super().__init__()
        self.register(Additor())
        self.register(Subtractor())