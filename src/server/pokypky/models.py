from pydantic import BaseModel
from datetime import date
from typing import Optional


class PokupkyInput(BaseModel):
    id_client: int
    id_medicine: int
    pokupka_date: date


class PokupkyOutput(BaseModel):
    id: int
    id_client: int
    id_medicine: int
    pokupka_date: date

