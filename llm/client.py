from openai import OpenAI
import os

class LLMCClient:
    def __init__(self):
        GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
        if not GITHUB_TOKEN:
            raise EnvironmentError("GITHUB_TOKEN environment variable is not set.")
        self.client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=GITHUB_TOKEN,
        )
