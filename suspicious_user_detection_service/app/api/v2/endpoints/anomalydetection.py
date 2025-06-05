from fastapi import APIRouter, File, Form, UploadFile
from app.models.anomaly import userPosts, AnomalyResponse
from app.services.scam_detector_agent import scam_detector_agent
from app.config.redis_client import redis_client, test_redis

router = APIRouter()

@router.post("/detect")
async def detect_suspicious_user(
    post_id: str = Form(...),
    post_type: str = Form(...),
    text: str = Form(...),
    item_type: str = Form(...),
    image_file: UploadFile = File(...)):


    return {"message": "Suspicious user detected"}


@router.get("/get/")
async def get_key():
    try:
        return await test_redis()
    except Exception as e:
        return {"error": str(e)}
