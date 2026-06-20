from llm.client import LLMClient
from llm.conversations import Conversation
from llm.prompts import EMAIL_CLASSIFICATION_PROMPT
from models.tickets import Ticket


class EmailServices:
    def __init__(self, llm_client: LLMClient | None = None):
        self.conversation = Conversation(
            client=(llm_client or LLMClient()).client,
            system_prompt=EMAIL_CLASSIFICATION_PROMPT,
        )

    def classify_email(self, email_content: str) -> Ticket:
        """Classify the email content and return a structured ticket."""
        return self.conversation.chat_structured(email_content, response_format=Ticket)
