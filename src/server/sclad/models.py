from pydantic import BaseModel

from typing import Optional


class ScladInput(BaseModel):
    id_medicine: int
    quantity: int


class ScladOutput(BaseModel):
    id: int
    id_medicine: int
    quantity: int

