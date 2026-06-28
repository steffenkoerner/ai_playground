from openai import OpenAI
from .config import GITHUB_TOKEN, BASE_URL


class LLMClient:
    def __init__(self):
        if not GITHUB_TOKEN:
            raise EnvironmentError("GITHUB_TOKEN environment variable is not set.")
        self.client = OpenAI(base_url=BASE_URL, api_key=GITHUB_TOKEN)
