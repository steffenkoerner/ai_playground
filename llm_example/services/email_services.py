from llm_example.llm.client import LLMClient
from llm_example.llm.conversations import Conversation
from llm_example.llm.prompts import EMAIL_CLASSIFICATION_PROMPT
from llm_example.models.tickets import Ticket


class EmailServices:
    def __init__(self, llm_client: LLMClient | None = None):
        self._client = (llm_client or LLMClient()).client

    def classify_email(self, email_content: str) -> Ticket:
        """Classify the email content and return a structured ticket."""
        # A fresh Conversation per call keeps each classification stateless.
        conversation = Conversation(client=self._client, system_prompt=EMAIL_CLASSIFICATION_PROMPT)
        return conversation.chat_structured(email_content, response_format=Ticket)
