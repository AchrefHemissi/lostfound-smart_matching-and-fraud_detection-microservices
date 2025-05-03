from fastapi import FastAPI
from app.api.v1.endpoints import embeddings , anomalydetection
from app.config.qdrant_config import initialize_qdrant_collection

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Initializing Qdrant collection...")
    initialize_qdrant_collection()

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the LostFound AI Service"}

app.include_router(embeddings.router, prefix="/api/v1/embedding")
app.include_router(anomalydetection.router, prefix="/api/v1/anomalydetection")