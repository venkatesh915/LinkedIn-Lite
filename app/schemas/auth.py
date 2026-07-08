from pydantic import BaseModel
from typing import Optional
class LoginRequest(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    #token_duration: int

class TokenData(BaseModel):
    email: Optional[str] | None = None
