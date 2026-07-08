#post table = postid, userid, content, image, createdAt 

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class PostBase(BaseModel):
    title: str
    content: str
    visibility: str = "public"

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    user_id: int
    content: str
    image_url: str| None = None
    likes_count: int = 0
    created_at: datetime
    
