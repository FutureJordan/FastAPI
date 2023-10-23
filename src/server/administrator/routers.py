from typing import List
from fastapi import APIRouter
from server.administrator.models import AdminInput, AdminOutput
from server.administrator.resolvers import get_admin, get_current_admin, add_admin, update_admin, delete_admin

router = APIRouter(prefix='/admins')


@router.get('/')
def get_admin_route() -> List[AdminOutput]:
    return get_admin()


@router.get('/{admin_id}')
def get_current_admin_route(admin_id: int) -> AdminOutput:
    return get_current_admin(admin_id)


@router.post('/')
def add_admin_route(new_admin: AdminInput):
    return add_admin(new_admin)


@router.put('/{admin_id}')
def update_admin_route(admin_id: int, new_admin: AdminInput) -> int:
    return update_admin(admin_id, new_admin)


@router.delete('/{admin_id}')
def delete_admin_route(admin_id: int) -> int:
    return delete_admin(admin_id)