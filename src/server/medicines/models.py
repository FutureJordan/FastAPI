from pydantic import BaseModel
from typing import Optional


class MedicineInput(BaseModel):
    title: str
    dosage: float
    type: str


class MedicineOutput(BaseModel):
    id: int
    title: str
    dosage: float
    type: str
