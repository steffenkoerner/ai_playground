from .agent.agent import Agent

def main():
    agent = Agent(name="Agent", model="gpt-4o-mini")
    response = agent.run("How is the weather in Munich?")
    print(response)


if __name__ == "__main__":
    main()
