from llm_example.services.embedding_services import EmbeddingServices
from llm_example.search.cosine import cosine_similarity


class SimilaritySearch:
    def __init__(self, documents: list[str], embedding_services: EmbeddingServices | None = None):
        self.embedding_services = embedding_services or EmbeddingServices()
        self.vector_store = self._build_index(documents)

    def _build_index(self, documents: list[str]) -> dict[str, list[float]]:
        return {doc: self.embedding_services.create_embedding(doc) for doc in documents}

    def similarity_search(self, query: str, top_k: int = 1) -> list[tuple[float, str]]:
        query_embedding = self.embedding_services.create_embedding(query)
        scores = [
            (cosine_similarity(query_embedding, emb), doc)
            for doc, emb in self.vector_store.items()
        ]
        scores.sort(reverse=True, key=lambda x: x[0])
        return scores[:top_k]
