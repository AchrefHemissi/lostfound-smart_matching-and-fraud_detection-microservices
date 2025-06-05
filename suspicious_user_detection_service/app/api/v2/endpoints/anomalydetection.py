from fastapi import APIRouter, File, Form, UploadFile
from app.models.anomaly import userPosts, AnomalyResponse
from app.services.scam_detector_agent import scam_detector_agent
from app.config.redis_client import redis_client, test_redis
from app.repositories.redis_repo import test

router = APIRouter()

@router.post("/detect")
async def detect_suspicious_user(
    post_id: str = Form(...),
    post_type: str = Form(...),
    text: str = Form(...),
    item_type: str = Form(...),
    image_file: UploadFile = File(...)):


    return {"message": "Suspicious user detected"}


@router.get("/test_redis/")
async def get_key():
    try:
        return await test_redis()
    except Exception as e:
        return {"error": str(e)}

@router.get("/test_repo/")
async def test_repo():
    try:
        await test()
    except Exception as e:
        return {"error": str(e)}