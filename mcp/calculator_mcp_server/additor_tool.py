from models.tools import Tool

class Additor(Tool):
    name: str = "add"
    description: str = "Adds two numbers together"

    def schema(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_number": {"type": "number"},
                        "second_number": {"type": "number"}
                    },
                    "required": ["first_number", "second_number"]
                }
            }
        }

    def execute(self, arguments):
        return arguments["first_number"] + arguments["second_number"]