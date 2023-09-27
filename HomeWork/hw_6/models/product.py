from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
