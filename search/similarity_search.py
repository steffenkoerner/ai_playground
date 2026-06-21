from examples.semantic_search import documents
from services.embedding_services import EmbeddingServices
from search.cosine import cosine_similarity

class SimilaritySearch:
    def __init__(self):
        self.embedding_services = EmbeddingServices()
        self.vector_store = self.init(documents)

    def init(self, documents):
        # Create embeddings for all documents and store them in a vector database
        result = {}
        for doc in documents:
            embedding = self.embedding_services.create_embedding(doc)
            # Store the embedding in a vector database (e.g., FAISS, Pinecone)
            # This is a placeholder for actual vector store implementation
            result[doc] = embedding
        return result

    def similarity_search(self, query):
        query_embedding = self.embedding_services.create_embedding(query)
        # Perform similarity search in the vector database using the query embedding
        # This is a placeholder for actual similarity search implementation
        similar_docs = []  # Retrieve similar documents based on cosine similarity or other metrics

        for (doc,embedding) in self.vector_store.items():
            similarity = cosine_similarity(query_embedding, embedding)
            similar_docs.append((similarity, doc))
        similar_docs.sort(reverse=True, key=lambda x: x[0])
        print(similar_docs)
        return similar_docs