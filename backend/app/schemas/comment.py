from datetime import datetime
from pydantic import BaseModel, ConfigDict


# Base Schema
class CommentBase(BaseModel):
    content: str


# Create Schema
class CommentCreate(CommentBase):
    user_id: int
    post_id: int


# Update Schema
class CommentUpdate(BaseModel):
    content: str


# Response Schema
class CommentResponse(CommentBase):
    id: int
    user_id: int
    post_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)