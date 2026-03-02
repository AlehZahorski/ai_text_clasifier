# Project: Ai Text Clasifier

## Goal

Build a production-ready AI microservice using FastAPI and LLMs.
Target role: AI Engineer / Applied AI Engineer.
Focus: enterprise-grade architecture, stability, observability.

---

## Current Architecture

### Stack

- Python 3.14
- FastAPI
- Pydantic v2
- OpenAI SDK
- python-dotenv
- Uvicorn

---

## Project Structure

app/
  api/
    routes.py
  services/
    text_service.py
    prompt_builder.py
  schemas/
    request_response.py
  core/
    config.py
  main.py

.env
requirements.txt

---

## Implemented Features

### 1. Endpoint: GET /health

Basic health check.

### 2. Endpoint: POST /classify

Input:
{
  "text": "some message"
}

Flow:
- request validation (Pydantic)
- build prompt (prompt_builder)
- call OpenAI API
- enforce JSON response_format
- parse JSON safely
- validate output using Pydantic
- log latency
- handle:
  - timeout
  - rate limit
  - API errors

Response:
{
  "category": "complaint | question | praise | other",
  "confidence": float
}

---

## Engineering Decisions

- No eval()
- JSON enforced via response_format
- Response validated before returning
- Config isolated in core/config.py
- Prompt separated from service logic
- Basic latency logging implemented

---

## Next Possible Steps

- Add /summarize endpoint
- Add retry with exponential backoff
- Centralized logging config
- Dockerfile + containerization
- Async version of service
- Unit tests
- RAG implementation
- Embeddings + vector store

---

## How to Continue Work

When starting a new ChatGPT session, paste:

---

Project: Enterprise AI Text Service  
Current state: classify endpoint with LLM, validation, logging, error handling  
Next goal: <write here what we want to implement today>

---

And continue from there.