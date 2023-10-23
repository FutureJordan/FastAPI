from pydantic import BaseModel
from typing import Optional


class ClientsInput(BaseModel):
    firstname: str
    lastname: str
    address: str
    phone: float


class ClientsOutput(BaseModel):
    id: int
    firstname: str
    lastname: str
    address: str
    phone: float
