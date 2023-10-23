from typing import List
from fastapi import APIRouter
from server.sclad.models import ScladInput, ScladOutput
from server.sclad.resolvers import get_sclad, get_current_sclad, add_sclads, update_sclad, delete_sclad

router = APIRouter(prefix='/sclads')


@router.get('/')
def get_sclad_route() -> List[ScladOutput]:
    return get_sclad()


@router.get('/{sclad_id}')
def get_current_sclad_route(sclad_id: int) -> ScladOutput:
    return get_current_sclad(sclad_id)


@router.post('/')
def add_sclad_route(new_sclad: ScladInput):
    return add_sclads(new_sclad)


@router.put('/{sclad_id}')
def update_sclad_route(sclad_id: int, new_sclad: ScladInput) -> int:
    return update_sclad(sclad_id, new_sclad)


@router.delete('/{sclad_id}')
def delete_sclad_route(sclad_id: int) -> int:
    return delete_sclad(sclad_id)
