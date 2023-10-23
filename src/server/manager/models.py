from pydantic import BaseModel
from typing import Optional

class ManagerInput(BaseModel):
    firstname: str
    lastname: str
    phone: float


class ManagerOutput(BaseModel):
    id: int
    firstname: str
    lastname: str
    phone: float
