# 🧠 lostfound-ai-service

A modular, scalable, and production-ready FastAPI microservice for generating and searching multimodal (image/text) embeddings using OpenAI’s CLIP model. Supports high-dimensional similarity search via Qdrant or FAISS.

---

## 📁 Project Structure

```
lostfound-ai-service/
│
├── app/
│   ├── main.py                     # FastAPI app entry point
│   │
│   ├── api/                        # API layer (HTTP routes and dependencies)
│   │   ├── v1/
│   │   │   └── endpoints/
│   │   │       └── embeddings.py   # V1 routes for embedding operations
│   │   ├── v2/
│   │   │   └── endpoints/
│   │   │       └── embeddings.py   # V2 routes for embedding operations
│   │   └── dependencies.py         # Shared dependencies (model loaders, DB clients, etc.)
│   │
│   ├── core/                       # App-wide configuration and settings
│   │   ├── config.py               # Loads environment variables and settings
│   │   ├── neo4j_config.py         # Neo4j DB client config (optional)
│   │   └── qdrant_config.py        # Qdrant vector store client config
│   │
│   ├── services/                   # Business logic and model interaction
│   │   ├── clip_service.py         # Handles CLIP model loading and inference
│   │   └── vector_service.py       # Vector DB operations (Qdrant, FAISS)
│   │
│   ├── models/                     # Pydantic request/response models
│   │   └── embedding_request.py    # Request schema for embedding endpoint
│
├── .env                            # Environment variables for local/dev
├── requirements.txt                # Project dependencies
└── README.md                       # This documentation file
```

---

## 🔍 Component Descriptions

- **`main.py`**  
  Initializes and runs the FastAPI app.

- **`api/v1/endpoints/embeddings.py`**  
  V1 embedding routes (standard CLIP use with basic inputs).

- **`api/v2/endpoints/embeddings.py`**  
  V2 routes with potential support for extended metadata or indexing.

- **`dependencies.py`**  
  Provides shared FastAPI `Depends` such as Qdrant, CLIP model, or Neo4j clients.

- **`core/config.py`**  
  Loads and validates configuration using `python-dotenv` and `pydantic`.

- **`services/clip_service.py`**  
  Loads the CLIP model, handles image/text preprocessing, and returns unified 512-dim embeddings.

- **`services/vector_service.py`**  
  Handles upsert, search, and delete operations on Qdrant or FAISS vector store.

---

## 🧰 Tech Stack & Tools

| Tool               | Purpose |
|--------------------|---------|
| **FastAPI**        | Web API framework |
| **Uvicorn**        | ASGI server |
| **PyTorch**        | Deep learning framework |
| **Torchvision**    | Preprocessing & image transforms |
| **Pillow**         | Image handling |
| **CLIP (OpenAI)**  | Embedding model (ViT-B/32) |
| **Qdrant**         | Scalable vector DB for similarity search |
| **Neo4j**          | Optional graph DB for similarity caching |
| **FAISS (optional)** | Local/dev vector search alternative |
| **python-dotenv**  | Loads environment variables from `.env` |

---

## ▶️ Getting Started

### 1. Create and activate a virtual environment

```bash
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file in the root with content similar to:

```env
QDRANT_HOST=http://localhost:6333
CLIP_MODEL=ViT-B/32
USE_FAISS=False
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
```

### 4. Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

## 👥 Authors

Developed by the FoundIt Team — INSAT 2025

---
