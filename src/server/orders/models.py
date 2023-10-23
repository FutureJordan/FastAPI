from pydantic import BaseModel
from datetime import date
from typing import Optional


class OrdersInput(BaseModel):
    id_client: int
    order_date: date


class OrdersOutput(BaseModel):
    id: int
    id_client: int
    order_date: date

