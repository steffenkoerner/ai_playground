from llm_example.services.email_services import EmailServices
from llm_example.search.similarity_search import SimilaritySearch
from llm_example.example_documents.semantic_search import documents


def classify_email():
    email_services = EmailServices()

    email_content = "My order #12345 arrived damaged and I want a replacement as soon as possible!"
    print(f"User: {email_content}\n")

    ticket = email_services.classify_email(email_content)

    print(f"Summary:         {ticket.summary}")
    print(f"Priority:        {ticket.priority.value}")
    print(f"Sentiment:       {ticket.sentiment.value}")
    print(f"Suggested reply: {ticket.suggested_reply}")

def similarity_search():
    similarity_search = SimilaritySearch(documents=documents)
    results = similarity_search.similarity_search("Reset password", top_k=3)
    for score, doc in results:
        print(f"{score:.4f}  {doc}")

    
    

if __name__ == "__main__":
    classify_email()
    print()
    print()
    print("Similarity Search Results:")
    similarity_search()


