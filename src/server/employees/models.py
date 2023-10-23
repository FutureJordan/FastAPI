from pydantic import BaseModel
from typing import Optional

class EmployeesInput(BaseModel):
    firstname: str
    lastname: str
    job: str
    phone: float


class EmployeesOutput(BaseModel):
    id: int
    firstname: str
    lastname: str
    job: str
    phone: float
