from typing import List
from fastapi import APIRouter
from server.clients.models import ClientsInput, ClientsOutput
from server.clients.resolvers import get_client, get_current_client, add_client, update_client, delete_client

router = APIRouter(prefix='/clients')


@router.get('/')
def get_client_route() -> List[ClientsOutput]:
    return get_client()


@router.get('/{client_id}')
def get_current_client_route(client_id: int) -> ClientsOutput:
    return get_current_client(client_id)


@router.post('/')
def add_client_route(new_client: ClientsInput):
    return add_client(new_client)


@router.put('/{client_id}')
def update_client_route(client_id: int, new_client: ClientsInput) -> int:
    return update_client(client_id, new_client)


@router.delete('/{client_id}')
def delete_client_route(client_id: int) -> int:
    return delete_client(client_id)
