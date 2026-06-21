from openai import OpenAI
from llm.client import LLMClient


class EmbeddingServices:
    def __init__(self):
        self.client = LLMClient()

    def create_embedding(self, text: str) -> list[float]:
        response = self.client.client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        embedding = response.data[0].embedding
        return embedding