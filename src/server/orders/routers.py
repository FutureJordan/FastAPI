from typing import List
from fastapi import APIRouter
from server.orders.models import OrdersInput, OrdersOutput
from server.orders.resolvers import get_order, get_current_orders, add_order, update_order, delete_orders

router = APIRouter(prefix='/orders')


@router.get('/')
def get_order_route() -> List[OrdersOutput]:
    return get_order()


@router.get('/{order_id}')
def get_current_order_route(orders_id: int) -> OrdersOutput:
    return get_current_orders(orders_id)


@router.post('/')
def add_order_route(new_order: OrdersInput):
    return add_order(new_order)


@router.put('/{order_id}')
def update_order_route(order_id: int, new_order: OrdersInput) -> int:
    return update_order(order_id, new_order)


@router.delete('/{order_id}')
def delete_order_route(order_id: int) -> int:
    return delete_orders(order_id)
