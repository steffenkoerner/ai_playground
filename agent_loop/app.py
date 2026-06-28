from agent_loop.agent import Agent
from agent_loop.mcp.servers.calculator_mcp_server import Additor
from agent_loop.mcp.servers.weather_mcp_server import WeatherTool

def main():
    agent = Agent(name="Agent", model="gpt-4o-mini")
    response = agent.run("How is the weather in Munich?")
    print(response)


if __name__ == "__main__":
    main()
