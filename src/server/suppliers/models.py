from pydantic import BaseModel
from typing import Optional


class SuppliersInput(BaseModel):
    title: str
    address: str
    phone: float


class SuppliersOutput(BaseModel):
    id: int
    title: str
    address: str
    phone: float
