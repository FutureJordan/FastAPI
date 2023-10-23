from typing import List
from fastapi import APIRouter
from server.manager.models import ManagerInput, ManagerOutput
from server.manager.resolvers import get_manager, get_current_manager, add_manager, update_manager, delete_manager

router = APIRouter(prefix='/managers')


@router.get('/')
def get_manager_route() -> List[ManagerOutput]:
    return get_manager()


@router.get('/{manager_id}')
def get_current_manager_route(manager_id: int) -> ManagerOutput:
    return get_current_manager(manager_id)


@router.post('/')
def add_manager_route(new_manager: ManagerInput):
    return add_manager(new_manager)


@router.put('/{manager_id}')
def update_manager_route(manager_id: int, new_manager: ManagerInput) -> int:
    return update_manager(manager_id, new_manager)


@router.delete('/{manager_id}')
def delete_manager_route(manager_id: int) -> int:
    return delete_manager(manager_id)