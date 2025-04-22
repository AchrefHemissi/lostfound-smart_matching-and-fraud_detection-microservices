from fastapi import FastAPI
from app.api.v1.endpoints import embeddings

app = FastAPI()

app.include_router(embeddings.router, prefix="/v1/embedding")