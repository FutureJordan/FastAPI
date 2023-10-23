from typing import List
from fastapi import APIRouter
from server.employees.models import EmployeesInput, EmployeesOutput
from server.employees.resolvers import get_employee, get_current_employee, add_employee, update_employee, delete_employee

router = APIRouter(prefix='/employees')


@router.get('/')
def get_employees_router() -> List[EmployeesOutput]:
    return get_employee()


@router.get('/{employee_id}')
def get_current_employee_route(employee_id: int) -> EmployeesOutput:
    return get_current_employee(employee_id)


@router.post('/')
def add_employee_route(new_employee: EmployeesInput):
    return add_employee(new_employee)


@router.put('/{employee_id}')
def update_employee_route(employee_id: int, new_employee: EmployeesInput) -> int:
    return update_employee(employee_id, new_employee)


@router.delete('/{employee_id}')
def delete_employee_route(employee_id: int) -> int:
    return delete_employee(employee_id)