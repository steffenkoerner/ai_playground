from .agent.agent import Agent
from .llm.client import LLMClient
from .mcp.client import MCPClient
from .mcp.servers.calculator_mcp_server.mcp_server import CalculatorMCPServer
from .mcp.servers.weather_mcp_server.mcp_server import WeatherMCPServer

def main():
    mcp_client = MCPClient()
    mcp_client.register(WeatherMCPServer())
    mcp_client.register(CalculatorMCPServer())
    llm_client = LLMClient()
    agent = Agent(name="Agent", llm_client=llm_client, mcp_client=mcp_client)
    response = agent.run("How is the weather in Munich?")
    print(response)


if __name__ == "__main__":
    main()
