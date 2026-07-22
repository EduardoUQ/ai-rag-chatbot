![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-black)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)

# 🤖 AI RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with **FastAPI**, **OpenAI**, **LangChain**, and **ChromaDB**.

The application allows users to ask questions about custom documents (PDFs), retrieving relevant information using semantic search before generating a response with OpenAI.

---

## Features

- REST API built with FastAPI
- Conversational memory using conversation IDs
- Retrieval-Augmented Generation (RAG)
- PDF ingestion
- Semantic search with embeddings
- ChromaDB vector database
- OpenAI GPT integration
- Docker support
- Interactive Swagger documentation

---

## Architecture

```
                User
                  │
                  ▼
            FastAPI API
                  │
                  ▼
            ChatService
          ┌──────────────┐
          ▼              ▼
ConversationManager   RAGService
                          │
                          ▼
                     ChromaDB
                          │
                          ▼
                      OpenAI API
```

---

## Technologies

- Python 3.12
- FastAPI
- OpenAI API
- LangChain
- ChromaDB
- Pydantic
- PyPDF
- Docker
- Uvicorn

---

## Project Structure

```text
app/
├── core/
├── ingestion/
├── models/
├── prompts/
├── routes/
├── services/
├── vectorstore/
└── main.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/EduardoUQ/ai-rag-chatbot

cd ai-rag-chatbot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key
```

---

## Ingest documents

Place your PDF files inside:

```text
data/
```

Run:

```bash
python -m app.ingestion.ingest
```

---

## Run locally

```bash
uvicorn app.main:app --reload
```

Swagger:

```
http://localhost:8000/docs
```

---

## Docker

Build the image:

```bash
docker build -t ai-rag-chatbot .
```

Run:

```bash
docker run --env-file .env -p 8000:8000 ai-rag-chatbot
```

---

## Example request

```http
POST /chat
```

```json
{
  "message": "What technologies does Eduardo know?"
}
```

Response:

```json
{
  "conversation_id": "...",
  "response": "..."
}
```

---

## What I learned

During this project I gained practical experience with:

- Building REST APIs using FastAPI.
- Integrating OpenAI models into production-style applications.
- Implementing conversational memory.
- Creating Retrieval-Augmented Generation (RAG) pipelines.
- Generating embeddings and performing semantic search with ChromaDB.
- Structuring Python applications using a layered architecture.
- Containerizing applications with Docker.

---

## Future Improvements

- Authentication
- Persistent conversation history
- Multiple document collections
- Streaming responses
- PostgreSQL + pgvector
- Web interface (React)
- User management

---

## Author

Eduardo Utrilla

LinkedIn:
https://www.linkedin.com/in/eduardo-utrilla/
