from pydantic import BaseModel
from typing import Optional


class AdminInput(BaseModel):
    firstname: str
    lastname: str
    phone: float


class AdminOutput(BaseModel):
    id: int
    firstname: str
    lastname: str
    phone: float
