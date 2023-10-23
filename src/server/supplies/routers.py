from typing import List
from fastapi import APIRouter
from server.supplies.models import SuppliesInput, SuppliesOutput
from server.supplies.resolvers import get_supplies, get_current_supplies, add_supplies, update_supplies, delete_supplies

router = APIRouter(prefix='/supplies')


@router.get('/')
def get_supplies_route() -> List[SuppliesOutput]:
    return get_supplies()


@router.get('/{supplies_id}')
def get_current_supplies_route(supplies_id: int) -> SuppliesOutput:
    return get_current_supplies(supplies_id)


@router.post('/')
def add_supplies_route(new_supplies: SuppliesInput):
    return add_supplies(new_supplies)


@router.put('/{supplies_id}')
def update_supplies_route(supplies_id: int, new_supplies: SuppliesInput) -> int:
    return update_supplies(supplies_id, new_supplies)


@router.delete('/{supplies_id}')
def delete_supplies_route(supplies_id: int) -> int:
    return delete_supplies(supplies_id)