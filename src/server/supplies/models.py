from pydantic import BaseModel
from typing import Optional


class SuppliesInput(BaseModel):
    id_supply: int
    id_medicine: int
    quantity: int
    

class SuppliesOutput(BaseModel):
    id: int
    id_supply: int
    id_medicine: int
    quantity: int

