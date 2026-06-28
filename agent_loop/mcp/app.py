from mcp.severs.weather_mcp_server.calculator_mcp_server.mcp_server import CalculatorMCPServer
from mcp.severs.weather_mcp_server.mcp_server import WeatherMCPServer
from mcp.client import MCPClient
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

    llm_client = LLMClient().client
    conversation = Conversation(client=llm_client, system_prompt="You are a helpful assistant")
    reply = conversation.chat_with_tools(user_message=user_message, tools=tools, tool_executor=mcp_client.call_tool)
    print(f"\n LLM reply: {reply}")


if __name__ == "__main__":
    question = "How is the weather in Munich?"
    main(question)
