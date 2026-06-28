from ....protocols.tools import Tool

class Subtractor(Tool):
    name: str = "subtract"
    description: str = "Subtracts two numbers"

     # This schema is currently derived manually, but in the future it will be derived from the function signature and docstring
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