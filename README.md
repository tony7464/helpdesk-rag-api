# Helpdesk RAG API

A Flask API from a Python lesson. It answers support questions from a small set of approved documents.

The retriever scores documents by keyword overlap. When it finds a match, the API sends a grounded prompt to a local [Ollama](https://ollama.com/) model (`llama3.2`). If nothing matches, it says so instead of guessing. Tests cover the `/api/ask` endpoint with pytest.

## Run

```bash
cd rag-helpdesk-api
pipenv install
pipenv run python app.py
```

Ollama has to be running locally with the `llama3.2` model pulled before `/api/ask` can draft an answer. Document lookup still works without it, and a missing model returns HTTP 503.

- Health check: `GET /api/health`
- Ask: `POST /api/ask` with JSON `{ "query": "How do I reset my password?" }`
