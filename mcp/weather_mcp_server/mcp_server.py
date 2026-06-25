from models.server import MCPServer
from weather_mcp_server.weather_tool import WeatherTool

class WeatherMCPServer(MCPServer):
    def __init__(self):
        super().__init__()
        self.register(WeatherTool())
