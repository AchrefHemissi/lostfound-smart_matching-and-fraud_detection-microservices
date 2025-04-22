from fastapi import APIRouter, HTTPException
from app.api.dependencies import get_firebase_post, generate_embedding, store_embedding, find_similar_embeddings

router = APIRouter()

@router.post("/generate/{post_id}")
async def generate(post_id: str):
    metadata = get_firebase_post(post_id)
    if not metadata:
        raise HTTPException(status_code=404, detail="Post not found")
    embedding = generate_embedding(metadata["image_url"], metadata["text"])
    store_embedding(post_id, embedding, metadata)
    return {"status": "success"}

@router.get("/similar/{post_id}")
async def get_similar(post_id: str):
    results = find_similar_embeddings(post_id)
    return {"results": results}