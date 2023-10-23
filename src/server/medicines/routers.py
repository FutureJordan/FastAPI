from typing import List
from fastapi import APIRouter
from server.medicines.models import MedicineInput, MedicineOutput
from server.medicines.resolvers import get_medicine, get_current_medicine, add_medicine, update_medicine, delete_medicine

router = APIRouter(prefix='/medicines')


@router.get('/')
def get_medicine_router() -> List[MedicineOutput]:
    return get_medicine()


@router.get('/{medicine_id}')
def get_current_medicine_route(medicine_id: int) -> MedicineOutput:
    return get_current_medicine(medicine_id)


@router.post('/')
def add_medicine_route(new_medicine: MedicineInput):
    return add_medicine(new_medicine)


@router.put('/{medicine_id}')
def update_medicine_route(medicine_id: int, new_medicine: MedicineInput) -> int:
    return update_medicine(medicine_id, new_medicine)


@router.delete('/{medicine_id}')
def delete_medicine_route(medicine_id: int) -> int:
    return delete_medicine(medicine_id)