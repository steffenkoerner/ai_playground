from ...protocols.server import MCPServer
from .weather_tool import WeatherTool

class WeatherMCPServer(MCPServer):
    def __init__(self):
        super().__init__()
        self.register(WeatherTool())
