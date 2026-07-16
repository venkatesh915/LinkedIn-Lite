from pydantic import BaseModel


class FollowCreate(BaseModel):
    follower_id: int
    following_id: int


class FollowUpdate(BaseModel):
    follower_id: int
    following_id: int