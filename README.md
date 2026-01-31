# RAG Assistant – PDF Question Answering

This project implements a Retrieval-Augmented Generation (RAG) system that answers user queries based on the content of PDF documents.

The system retrieves relevant document chunks using semantic search and generates grounded answers using a Large Language Model (LLM).

---

## Features

- PDF ingestion and text chunking
- Semantic search using embeddings and FAISS
- Query rewriting for improved retrieval quality
- Context-grounded answer generation
- Source attribution for transparency
- Gradio-based interactive user interface
- FastAPI backend for API access

---

## Architecture Flow

PDFs → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add PDF documents

Place your PDF files inside:
```bash
data/docs/
```

### 3. Ingest documents
```bash
python ingest.py
```

This step extracts text from PDFs, create embeddings, and store them in FAISS vector index.

---

## Running the Application
### Run Gradio UI
```bash
python app.py
```

Then open the provided local URL in your browser and start asking questions.

---

## Usage Demo

https://youtu.be/BePgjtI-Wvw

## Notes

FAISS is used for local prototyping due to its simplicity and speed. The vector store layer is modular and can be replaced with production-grade systems such as Qdrant or Pinecone without changing the core RAG pipeline.


## Future Improvements

- Replace FAISS with a production-grade vector database (Qdrant / Pinecone)
- Add chat history and multi-turn conversations
- Stream LLM responses
- Support runtime document uploads








