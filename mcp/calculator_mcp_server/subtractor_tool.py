from models.tools import Tool

class Subtractor(Tool):
    name: str = "subtract"
    description: str = "Subtracts two numbers"

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
        return arguments["first_number"] - arguments["second_number"]