from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: str
    status: str
