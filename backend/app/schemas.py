from pydantic import BaseModel, EmailStr
from typing import Optional, List, Any

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AddressCreate(BaseModel):
    address: str
    chain: str
    category: Optional[str] = "unknown"
    tags: Optional[str] = ""

class AddressOut(BaseModel):
    id: int
    address: str
    chain: str
    category: str
    risk_score: float
    tags: str
    metadata: Any
    date_added: str
    class Config:
        orm_mode = True