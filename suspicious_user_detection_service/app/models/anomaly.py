from pydantic import BaseModel, Field, HttpUrl
from typing import Literal, Optional, Dict, Any, List
from datetime import datetime

class Post(BaseModel):
    id: str
    date : str 
    image_url: Optional[str] = None
    description: Optional[str] = None

class userPosts(BaseModel):
    user_id: str  # Changed to snake_case for consistency
    posts: List[Post]  # Now uses the Post model instead of generic dict

class AnomalyResponse(BaseModel):
    flagged: bool
    suspicious_score: int
    suspicious_reasons: List[str]
