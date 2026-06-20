"""
Send a message to an LLM using GitHub Models API (uses your GitHub Copilot token).

Setup:
1. Create a GitHub PAT at https://github.com/settings/tokens
   - Classic token: no special scopes needed (free tier uses GitHub identity)
   - OR use a fine-grained token
2. Export the token:
      export GITHUB_TOKEN="your_token_here"
3. Install dependencies:
      pip install openai

Available models (see https://github.com/marketplace/models):
  - gpt-4o, gpt-4o-mini
  - Meta-Llama-3.1-70B-Instruct
  - Mistral-large, Mistral-small
  - claude-3-5-sonnet (if available to your account)
"""

from services.email_services import EmailServices
from models.tickets import Ticket,Enum



if __name__ == "__main__":


    user_message = "My order #12345 arrived damaged and I want a replacement as soon as possible!"
    print(f"User: {user_message}\n")
    email_services = EmailServices()
    ticket: Ticket = email_services.classify_email(user_message)
    #ticket: Ticket = customer_support.chat(user_message, response_format=Ticket)

    print(f"Summary:         {ticket.summary}")
    print(f"Priority:        {ticket.priority.value}")
    print(f"Sentiment:       {ticket.sentiment.value}")
    print(f"Suggested reply: {ticket.suggested_reply}")
