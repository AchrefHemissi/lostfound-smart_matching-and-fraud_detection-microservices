Here’s a full breakdown of the project architecture:

📦 Project: lostfound-ai-service  
This service allows users to generate and search image/text embeddings using OpenAI’s CLIP model and a vector store which is Qdrant. It’s designed to be modular, scalable, and production-ready.

📁 Root Structure:

lostfound-ai-service/  
│  
├── app/ # Main application package  
│ ├── main.py # Entry point that creates and runs the FastAPI app  
│ │  
│ ├── api/ # API layer - HTTP routes & dependencies  
│ │ ├── v1/ # Versioned API (e.g. /v1/embedding)  
│ │ │ └── endpoints/ # All versioned route handlers  
│ │ │ └── embeddings.py # Defines routes for text/image embedding  
│ │ └── dependencies.py # Shared dependency injection (e.g., model loader, DB session)  
│ │  
│ ├── core/ # Core configuration utilities  
│ │ ├── config.py # Loads environment variables and app settings  
│ │ └── logger.py # Standardized logging configuration  
│ │  
│ ├── services/ # Business logic and services  
│ │ ├── clip_service.py # Handles CLIP model loading and embedding generation  
│ │ └── vector_service.py # Handles vector indexing and similarity search (Qdrant/FAISS)  
│ │  
│ ├── models/ # Pydantic schemas for validation and serialization  
│ │ └── embedding_request.py # Request and response models for embedding API  
│ │  
│ └── utils/ # Utility modules and helpers  
│ └── image_utils.py # Image pre-processing and formatting for the CLIP model  
│  
├── tests/ # Unit and integration test suite  
│ ├── test_clip_service.py # Tests for embedding logic  
│ └── test_vector_service.py # Tests for vector search logic  
│  
├── test_images/ # Sample images for testing embedding/search  
├── .env # Environment variables (e.g., vector DB URL, settings)  
├── requirements.txt # List of required Python packages  
└── README.md # Project documentation and setup guide

🔍 Breakdown of Core Roles:

- app/main.py  
  Initializes and runs the FastAPI app. Wires routes, middleware, and config.

- app/api/  
  Defines all HTTP-accessible functionality. This is the "controller" layer that communicates between the outside world and internal logic.

- app/api/v1/endpoints/embeddings.py  
  Defines POST routes to process user requests (like uploading an image or text to embed it).

- app/api/dependencies.py  
  Provides reusable FastAPI dependencies — like a loaded model, DB session, or shared configs.

- app/core/  
  Everything related to core app behavior — config loading and logging. This makes it easy to centralize things like env parsing and system diagnostics.

- app/services/  
  Encapsulates the logic for interacting with models and vector databases. Think of these as the brains of the app — where embeddings are generated and searched.

- app/models/  
  Defines the data shape that your API expects or returns. Keeps I/O clean and strongly validated.

- app/utils/  
  Utility helpers — usually stateless functions for tasks like image resizing, normalization, etc.

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
source venv/bin/activate # on Mac/Linux

# or

venv\Scripts\activate # on Windows

pip install -r requirements.txt
