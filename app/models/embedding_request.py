from pydantic import BaseModel

class EmbeddingRequest(BaseModel):
    post_id: str
    image_url: str
    text: str