from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=6)