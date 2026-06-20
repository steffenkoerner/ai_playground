from llm.client import LLMCClient
from models.tickets import Ticket
from llm.prompts import SYSTEM_PROMPT

class EmailServices:
    def __init__(self):
        self.client = LLMCClient().client
        self.response_format = Ticket  # Pydantic model for structured output

    def classify_email(self, email_content: str) -> str:
        """
        Classify the email content and return a structured ticket.
        """

        response = self.client.beta.chat.completions.parse(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": email_content}],
                response_format=self.response_format,
            )
        reply = response.choices[0].message.parsed
        return reply