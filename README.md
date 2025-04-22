Here’s a full breakdown of the project architecture:

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
│   │
│   ├── core/               # Core settings and configuration
│   │   ├── config.py       # Loads environment variables and app settings
│   │   └── logger.py       # App-wide logging configuration
│   │
│   ├── services/           # Core business logic
│   │   ├── clip_service.py     # CLIP model loading and embedding
│   │   └── vector_service.py   # Vector database (Qdrant/FAISS) operations
│   │
│   ├── models/             # Pydantic request/response models
│   │   └── embedding_request.py
│   │
│   └── utils/              # Utility functions
│       └── image_utils.py  # Image preprocessing for CLIP
│
├── tests/                  # Unit and integration tests
│   ├── test_clip_service.py
│   └── test_vector_service.py
│
├── test_images/            # Sample images for testing
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

- **app/api/dependencies.py**  
  Reusable FastAPI dependencies like model loaders, DB sessions.

- **app/core/**  
  Environment configuration and logging setup.

- **app/services/**  
  Main logic for interacting with CLIP and the vector store.

- **app/models/**  
  Pydantic schemas for request validation and response shaping.

- **app/utils/**  
  Utility helpers like image pre-processing.

- tests/  
  Contains all unit and integration tests to ensure the code works correctly and reliably.

Those are the main tools used on this project :

fastapi
🚀 What: A modern web framework for building APIs with Python 3.7+
📌 Why: You'll use FastAPI to expose your AI model as an API endpoint (e.g., receive a post and return similar items).
✅ Chosen because it's fast, async-ready, easy to document, and great for microservices.

uvicorn
🚀 What: A lightning-fast ASGI server to run FastAPI apps
📌 Why: FastAPI needs an ASGI server to run. Uvicorn handles incoming requests and serves your app.
✅ Chosen for its performance and compatibility with FastAPI.

torch
🧠 What: PyTorch, a deep learning framework
📌 Why: CLIP (the model you'll use for embeddings) is built on PyTorch.
✅ Chosen because CLIP depends on it, and it’s widely used for deep learning.

torchvision
🖼️ What: PyTorch’s library for image transformations and pretrained models
📌 Why: Required by CLIP and helpful for processing images before passing them into the model.
✅ Chosen because it complements PyTorch perfectly for image tasks.

faiss-cpu
🔍 What: Facebook AI Similarity Search — a library for fast vector search
📌 Why: You need to find similar vectors (image+text embeddings). FAISS does this super fast, especially on large datasets.
✅ Chosen for performance in similarity search. You’re using the CPU version for local/dev simplicity.

pillow
🖼️ What: A Python image processing library
📌 Why: You'll need to load and manipulate images before feeding them to CLIP.
✅ Chosen because it's lightweight, easy to use, and commonly used for image I/O.

python-dotenv
🔐 What: Loads environment variables from a .env file
📌 Why: You’ll likely want to keep secrets (e.g., API keys, config options) outside your code.
✅ Chosen because it's simple and helps you follow 12-factor app practices.

git+https://github.com/openai/CLIP.git
🧠 What: The actual CLIP model (Contrastive Language–Image Pre-training) by OpenAI
📌 Why: This is the model you're using to create shared embeddings from text & images.
✅ Chosen because CLIP is state-of-the-art for aligning images and text in the same embedding space.

qdrant-client
🧠 What: Python SDK for Qdrant — a vector database
📌 Why: You might store embeddings in a vector DB instead of just FAISS (better for production, filtering, metadata, etc).
✅ Chosen because Qdrant is modern, open-source, fast, and offers filtering + metadata support.

How to run the project

python -m venv venv
venv\Scripts\activate

````

### 2. Install dependencies

```bash
pip install -r requirements.txt
````
