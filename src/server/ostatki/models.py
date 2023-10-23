from pydantic import BaseModel

from typing import Optional


class OstatkiInput(BaseModel):
    id_medicine: int
    quantity: int


class OstatkiOutput(BaseModel):
    id: int
    id_medicine: int
    quantity: int

