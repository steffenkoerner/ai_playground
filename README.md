# From Software Engineer to AI Systems Engineer

A collection of hands-on experiments exploring practical LLM patterns in Python — structured output, multi-turn conversations, semantic search, and embeddings — all powered by the [GitHub Models API](https://github.com/marketplace/models) using your existing GitHub Copilot subscription.

---

## Use Cases

### 1. Email Classification
Classify customer emails into structured support tickets using LLM structured output.  
The model reads a raw email and returns a validated Pydantic object — no fragile JSON parsing, no prompt-engineering the output format.

```
"My order arrived damaged!" 
        ↓  gpt-4o-mini + structured output
Ticket(summary="Damaged order...", priority=HIGH, sentiment=NEGATIVE, suggested_reply="...")
```

### 2. Semantic Similarity Search
Find the most relevant document for a query using text embeddings and cosine similarity — a minimal vector search implementation from scratch.

```
Query: "Reset password"
        ↓  text-embedding-3-small + cosine similarity
0.8812  "Reset your password by clicking Forgot Password."
0.2341  "Employees receive 30 vacation days."
...
```

---

## Setup

**Prerequisites:** Python 3.11+, a GitHub account with Copilot access.

### 1. Clone and install dependencies

```bash
git clone https://github.com/your-username/ai_playground.git
cd ai_playground
pip install -r requirements.txt
```

### 2. Get a GitHub Personal Access Token

Go to [github.com/settings/tokens](https://github.com/settings/tokens) → *Generate new token (classic)*.  
No special scopes are needed — your GitHub identity grants access to GitHub Models.

### 3. Export the token

```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

### 4. Run

```bash
# Semantic similarity search (default)
python app.py

# Email classification — uncomment classify_email() in app.py
python app.py
```

---

## Project Structure

```
ai_playground/
├── app.py                    # Entry point — wire up and run use cases
├── config.py                 # Central config: model names, API base URL
├── requirements.txt
│
├── llm/                      # LLM infrastructure layer
│   ├── client.py             # OpenAI client wrapper (GitHub Models endpoint)
│   ├── conversations.py      # Multi-turn chat session with history management
│   └── prompts.py            # Prompt constants, one per use case
│
├── models/                   # Pydantic output schemas
│   └── tickets.py            # Ticket, Priority, Sentiment
│
├── services/                 # Business logic (LLM-agnostic interface)
│   ├── email_services.py     # classify_email() → Ticket
│   └── embedding_services.py # create_embedding() → list[float]
│
├── search/                   # Similarity search
│   ├── cosine.py             # Cosine similarity (numpy)
│   └── similarity_search.py  # Index documents, query top-k
│
└── examples/
    └── semantic_search.py    # Sample document corpus
```

---

## Architecture

The codebase follows a layered architecture where each layer only depends on the one below it:

```
app.py  (entry point)
   └── services/  (business logic — no LLM details)
          └── llm/  (LLM infrastructure — client, conversations, prompts)
                └── config.py  (settings)
```

Key design decisions:
- **Services don't expose LLM internals.** `EmailServices.classify_email()` returns a `Ticket` — the caller doesn't know or care that an LLM is involved.
- **Dependency injection.** Every service accepts an optional `llm_client` parameter, making it easy to swap implementations or mock in tests.
- **Structured output over prompt engineering.** `client.beta.chat.completions.parse()` sends the Pydantic schema to the API automatically and returns a validated object — no manual JSON parsing.

---

## Key Concepts Demonstrated

| Concept | Where |
|---|---|
| Structured output with Pydantic | `llm/conversations.py` → `chat_structured()` |
| Multi-turn conversation history | `llm/conversations.py` → `Conversation` |
| Text embeddings | `services/embedding_services.py` |
| Cosine similarity from scratch | `search/cosine.py` |
| Semantic vector search | `search/similarity_search.py` |
| Dependency injection | `services/email_services.py`, `services/embedding_services.py` |
| Enum-constrained Pydantic models | `models/tickets.py` |

---

## Models Used

| Model | Purpose |
|---|---|
| `gpt-4o-mini` | Email classification (chat + structured output) |
| `text-embedding-3-small` | Generating text embeddings for similarity search |

Both are available on [GitHub Models](https://github.com/marketplace/models) at no extra cost with a GitHub Copilot subscription.

