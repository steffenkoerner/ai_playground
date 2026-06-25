import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from calculator_mcp_server.mcp_server import CalculatorMCPServer
from weather_mcp_server.mcp_server import WeatherMCPServer
from client import MCPClient
from llm.client import LLMClient
from llm.conversations import Conversation

def main(user_message: str):
    calculator_server = CalculatorMCPServer()
    weather_server = WeatherMCPServer()
    mcp_client = MCPClient()
    mcp_client.register(calculator_server)
    mcp_client.register(weather_server)

    tools = mcp_client.list_tools()
   
    print("Available tools:", tools)


    # Pass the tools to the llm and let it decide which tool to call based on the user input
    llm_client = LLMClient().client
    conversation = Conversation(client=llm_client, system_prompt="You are a helpful assistant")
    reply = conversation.chat_with_tools(user_message=user_message, tools=tools, tool_executor=mcp_client.call_tool)
    print(f"\n LLM reply: {reply}")


if __name__ == "__main__":
    question = "How is the weather in Munich?"
    main(question)
