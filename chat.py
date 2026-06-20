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

import os
from openai import OpenAI

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise EnvironmentError("GITHUB_TOKEN environment variable is not set.")

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)

class Assistant:
    def __init__(self, name: str = "Assistant", system_prompt: str = "You are a helpful assistant."):
        self.name = name
        self.system_prompt = system_prompt
        self.system_prompt = [{"role": "system", "content": self.system_prompt}]


    def chat(self, messages: list, model: str = "gpt-4o-mini") -> str:
        response = client.chat.completions.create(
            model=model,
            messages= self.system_prompt + messages
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    user_message = "Hallo! Wie gehts."
    print(f"User: {user_message}\n")
    spanish_assistant = Assistant(name="Spanish Assistant", system_prompt="You are a helpful assistant that responds in Spanish.")
    messages=[        
            {"role": "user", "content": user_message},
        ]
    reply = spanish_assistant.chat(messages)

    print(f"Assistant: {reply}")
