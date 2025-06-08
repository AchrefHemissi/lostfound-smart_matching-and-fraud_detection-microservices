
# 🧠 lostfound-ai-service

A modular FastAPI microservice for generating and searching image/text embeddings using OpenAI’s CLIP model and a vector store (Qdrant). Designed to be scalable and production-ready.

---

## 📁 Project Structure

```text
lostfound-ai-service/
│
├── app/                     # Main application code
│   ├── main.py             # FastAPI app entry point
│   │
│   ├── api/                # API layer (HTTP routes and dependencies)
│   │   ├── v1/
│   │   │   └── endpoints/
│   │   │       └── embeddings.py   # API routes for text/image embedding
│   │   └── dependencies.py         # Shared dependencies (model loaders, DB, etc.)
|   |   ├── v2/
│   │   │   └── endpoints/
│   │   │       └── embeddings.py   # API routes for text/image embedding
│   │   └── dependencies.py         # Shared dependencies (model loaders, DB, etc.)
│   │
│   ├── core/               # Core settings and configuration
│   │   ├── config.py       # Loads environment variables and app settings
│   │   |
|   |   ├── neo4j_config.py 
|   |   |
|   |   ├──qdrant_config.py
│   │
│   ├── services/           # Core business logic
│   │   ├── clip_service.py     # CLIP model loading and embedding
│   │   └── vector_service.py   # Vector database (Qdrant/FAISS) operations
│   │
│   ├── models/             # Pydantic request/response models
│   │   └── embedding_request.py
│
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and instructions
```

---

## 🔍 Component Descriptions

- **app/main.py**  
  Initializes and runs the FastAPI app.

- **app/api/**  
  Defines all HTTP-accessible routes and shared dependencies.

- **app/api/v1/endpoints/embeddings.py**  
  POST endpoints to embed images or text.
  
- **app/api/v2/endpoints/embeddings.py**  
  POST endpoints to embed images or text.

- **app/api/dependencies.py**  
  Reusable FastAPI dependencies like model loaders, DB sessions.

- **app/core/**  
  Environment configuration and logging setup.

- **app/services/**  
  Main logic for interacting with CLIP and the vector store.

- **app/models/**  
  Pydantic schemas for request validation and response shaping.

---

## 🧰 Tech Stack & Tools

| Tool               | Description |
|--------------------|-------------|
| **FastAPI**        | 🚀 High-performance Python web framework used to expose the API. |
| **Uvicorn**        | ⚡ ASGI server to run FastAPI apps. |
| **PyTorch**        | 🧠 Deep learning framework used by CLIP. |
| **Torchvision**    | 🖼️ Image utilities and pretrained models required by CLIP. |
| **FAISS (faiss-cpu)** | 🔍 Fast vector similarity search (for local/dev use). |
| **Pillow**         | 🖼️ Image loading and processing. |
| **python-dotenv**  | 🔐 Loads secrets and environment variables from `.env`. |
| **CLIP (OpenAI)**  | 📷📝 Creates shared embeddings for images and text. |
| **Qdrant**         | 📦 Vector database for storing and searching embeddings (alternative to FAISS). |

---

## ▶️ Running the Project

### 1. Create and activate a virtual environment

```bash
# On macOS/Linux:
python -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the app

```bash
uvicorn app.main:app --reload
```
