# Tavus RAG Chatbot

## Overview

Tavus RAG Chatbot is a real-time conversational AI assistant that combines avatar-based interactions with Retrieval-Augmented Generation (RAG).

The system integrates Tavus, FastAPI, Elasticsearch vector search, LangChain, and OpenAI GPT-4.1 to deliver context-aware responses grounded in a custom knowledge base.

The project demonstrates the implementation of a production-style AI pipeline involving semantic search, prompt orchestration, and streaming LLM responses.

---

## Features

* Real-time conversational AI
* Tavus avatar integration
* Retrieval-Augmented Generation (RAG)
* Elasticsearch vector search using cosine similarity
* OpenAI GPT-4.1 integration
* Streaming responses via FastAPI
* Modular service architecture
* Environment-based configuration

---

## Architecture

```text
User
  │
  ▼
Frontend UI
  │
  ▼
Create Conversation API
  │
  ▼
Tavus Platform
  │
  ▼
FastAPI Backend
  │
  ▼
Embedding Generation
  │
  ▼
Elasticsearch Vector Search
  │
  ▼
GPT-4.1
  │
  ▼
Streaming Response
  │
  ▼
Tavus Avatar
```

---

## Tech Stack

### Backend

* Python
* FastAPI

### AI Components

* OpenAI GPT-4.1
* LangChain

### Retrieval Layer

* Elasticsearch Vector Database
* Cosine Similarity Search

### Integration

* Tavus

---

## Request Flow

1. User sends a message through Tavus.
2. FastAPI receives the request.
3. User query is converted into an embedding.
4. Elasticsearch performs semantic vector search.
5. Relevant documents are retrieved.
6. Context is injected into a prompt template.
7. GPT-4.1 generates an answer.
8. Response is streamed back to Tavus.
9. Tavus presents the answer to the user.

---

## Example Use Cases

* Healthcare benefits assistant
* Insurance plan support
* Knowledge base search
* Customer support automation
* Product information retrieval

---

## Project Structure

```text
app/
├── chains/
├── prompts/
├── routes/
├── services/
└── main.py
```

---

## Installation

```bash
git clone https://github.com/yourusername/tavus-rag-chatbot.git

cd tavus-rag-chatbot

pip install -r requirements.txt
```

Create a .env file:

```env
OPENAI_API_KEY=your_key

ELASTIC_HOST=http://localhost:9200

ELASTIC_USER=elastic

ELASTIC_PASSWORD=password
```

Run the application:

```bash
uvicorn app.main:app --reload
```

---

## Future Improvements

* Conversation memory
* Multi-agent orchestration
* Hybrid search (BM25 + Vector Search)
* Docker deployment
* Azure OpenAI support
* Observability and tracing

---

## Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation
* Vector databases
* Semantic search
* LLM integrations
* Streaming APIs
* FastAPI development
* Conversational AI systems
