from typing import List
from fastapi import APIRouter
from server.pokypky.models import PokupkyInput, PokupkyOutput
from server.pokypky.resolvers import get_pokupky, get_current_pokypky, add_pokupky, update_pokupky, delete_pokupky

router = APIRouter(prefix='/pokupky')


@router.get('/')
def get_pokupky_route() -> List[PokupkyOutput]:
    return get_pokupky()


@router.get('/{pokupky_id}')
def get_current_pokupky_route(pokupka_id: int) -> PokupkyOutput:
    return get_current_pokypky(pokupka_id)


@router.post('/')
def add_pokupky_route(new_pokupka: PokupkyInput):
    return add_pokupky(new_pokupka)


@router.put('/{pokupka_id}')
def update_pokupky_route(pokupka_id: int, new_pokupka: PokupkyInput) -> int:
    return update_pokupky(pokupka_id, new_pokupka)


@router.delete('/{pokupka_id}')
def delete_pokupky_route(pokupka_id: int) -> int:
    return delete_pokupky(pokupka_id)
