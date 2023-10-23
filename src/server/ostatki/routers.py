from typing import List
from fastapi import APIRouter
from server.ostatki.models import OstatkiInput, OstatkiOutput
from server.ostatki.resolvers import get_ostatki, get_current_ostatki, add_ostatki, update_ostatki, delete_ostatki

router = APIRouter(prefix='/ostatki')


@router.get('/')
def get_ostatki_route() -> List[OstatkiOutput]:
    return get_ostatki()


@router.get('/{ostatok_id}')
def get_current_ostatki_route(ostatok_id: int) -> OstatkiOutput:
    return get_current_ostatki(ostatok_id)


@router.post('/')
def add_ostatki_route(new_ostatok: OstatkiInput):
    return add_ostatki(new_ostatok)


@router.put('/{ostatok_id}')
def update_ostatki_route(ostatok_id: int, new_ostatok: OstatkiInput) -> int:
    return update_ostatki(ostatok_id, new_ostatok)


@router.delete('/{ostatok_id}')
def delete_ostatki_route(ostatok_id: int) -> int:
    return delete_ostatki(ostatok_id)
