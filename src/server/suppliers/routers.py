from typing import List
from fastapi import APIRouter
from server.suppliers.models import SuppliersInput, SuppliersOutput
from server.suppliers.resolvers import get_supplier, get_current_supplier, add_supplier, update_supplier, delete_supplier

router = APIRouter(prefix='/suppliers')


@router.get('/')
def get_supplier_router() -> List[SuppliersOutput]:
    return get_supplier()


@router.get('/{supplier_id}')
def get_current_supplier_router(supplier_id: int) -> SuppliersOutput:
    return get_current_supplier(supplier_id)


@router.post('/')
def add_supplier_router(new_supplier: SuppliersInput):
    return add_supplier(new_supplier)


@router.put('/{supplier_id}')
def update_supplier_route(supplier_id: int, new_supplier: SuppliersInput) -> int:
    return update_supplier(supplier_id, new_supplier)


@router.delete('/{supplier_id}')
def delete_suppliers_router(supplier_id: int) -> int:
    return delete_supplier(supplier_id)