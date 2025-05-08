from fastapi import FastAPI
from app.api.v1.endpoints import anomalydetection

app = FastAPI()


    

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the suspicious_user_detection_service AI Service"}

app.include_router(anomalydetection.router, prefix="/api/v1/anomalydetection")