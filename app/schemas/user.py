from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


#Base User Model 
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    username: str


#Model for creating a New User
class UserCreate(UserBase):
    password: str


#Model for returning user data
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    model_config = ConfigDict(
        from_attributes=True
    )

#Model for updating user profile
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    profile_image_url: Optional[str] = None
