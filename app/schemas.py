from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


    class Config:
        orm_mode = True

class BaseUser(BaseModel):
    email: EmailStr
    password : str

class UserCreate(BaseUser):
     pass

class UserLogin(BaseUser):
    pass

class User(BaseModel):
    id: int
    email: EmailStr
    created_at : datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner : User

    class Config:
        orm_mode = True

class PostVote(BaseModel):
    Post: Post
    votes: int

class Token(BaseModel):
    access_token : str
    token_type : str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id : Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)