from datetime import datetime
from pydantic import BaseModel


class UserBasse(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class User(BaseModel):
    username: str

    class Config:
        from_attributes = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User

    class Config:
        from_attributes = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True
