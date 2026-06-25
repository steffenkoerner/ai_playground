from ..models.tools import Tool
class WeatherTool(Tool):
    name: str = "get_weather"
    description: str = "Returns weather for a city"

    def schema(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"}
                    },
                    "required": ["city"]
                }
            }
        }

    def execute(self, arguments):
        return f"Weather in {arguments['city']}: 22°C"