# AI Ops Assistant

A multi-tool, memory-persistent AI agent that combines three earlier projects
(RAG, an autonomous LangGraph agent, and a classical ML API) into a single
system with a real chat interface. Instead of a fixed pipeline, the agent
decides for itself which tool a question requires.

## What it can do

- **`dokuman_ara`** — searches this system's own internal project docs
  (embeddings + cosine similarity, the same approach as
  [CitePilot](https://github.com/Phaldors/citepilot-rag)).
- **`web_ara`** — searches the live web via DuckDuckGo (no API key needed)
  for current/general knowledge.
- **`ariza_tahmini`** — calls a trained `RandomForestClassifier` (same
  approach as
  [Predictive Maintenance API](https://github.com/Phaldors/predictive-maintenance-api))
  to predict machine failure risk from sensor readings.
- **Persistent memory** — conversation history is checkpointed to SQLite
  per `thread_id`, so the agent remembers earlier turns in the same
  conversation.
- **Real chat UI** — a plain HTML/CSS/JS frontend served by FastAPI.

The agent picks the right tool itself based on each tool's description; a
notable bug found and fixed during development was the agent confusing our
own "CitePilot" project with an unrelated real-world product of the same
name, calling `web_ara` instead of `dokuman_ara` — fixed by sharpening the
tool description and adding a system prompt.

## Run it locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app/train_maintenance.py   # trains and saves maintenance_model.pkl
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/`.

## Run it with Docker

```bash
docker build -t ai-ops-assistant .
docker run -p 8000:8000 -e OPENAI_API_KEY=your-key-here ai-ops-assistant
```

## Stack

Python, LangGraph, LangChain (`create_agent`), OpenAI API, scikit-learn,
FastAPI, SQLite (checkpointing), Docker.
