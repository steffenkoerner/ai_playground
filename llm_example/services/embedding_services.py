from llm_example.llm.client import LLMClient
from llm_example.config import EMBEDDING_MODEL


class EmbeddingServices:
    def __init__(self, llm_client: LLMClient | None = None):
        self.client = (llm_client or LLMClient()).client

    def create_embedding(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            input=text,
            model=EMBEDDING_MODEL,
        )
        return response.data[0].embedding