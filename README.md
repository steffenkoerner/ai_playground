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

### 3. MCP (Model Context Protocol)
A minimal MCP implementation demonstrating how tools are exposed to an LLM without the LLM knowing anything about the protocol itself. The MCP layer handles tool registration, schema generation, and dispatching — the LLM just sees a list of callable functions and decides which one to invoke.

```
"How is the weather in Munich?"
        ↓  MCP client resolves tools from registered servers
        ↓  gpt-4o-mini selects and calls get_weather(city="Munich")
        ↓  WeatherMCPServer executes the tool and returns the result
"The weather in Munich is 22°C."
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
# Semantic similarity search and email classification
python app.py

# mcp example
python -m mcp.app
```



## Models Used

| Model | Purpose |
|---|---|
| `gpt-4o-mini` | Email classification (chat + structured output) |
| `text-embedding-3-small` | Generating text embeddings for similarity search |
| `gpt-4o-mini` | MCP tool-calling agent |

Both are available on [GitHub Models](https://github.com/marketplace/models) at no extra cost with a GitHub Copilot subscription.

