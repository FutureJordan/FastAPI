from server.database.db_manager import base_manager
from server.employees.models import EmployeesOutput, EmployeesInput


def get_employee():
    res = base_manager.execute("SELECT id, firstname, lastname, job, phone FROM employees", many=True)
    print(res)
    employees = []
    if not res:
        return None
    for employee in res['data']:
        employees.append(EmployeesOutput(id=employee[0], firstname=employee[1], lastname=employee[2], job=employee[3], phone=employee[4]))
    return employees


def get_current_employee(employee_id: int):
    res = base_manager.execute("SELECT id, firstname, lastname, job, phone FROM employees WHERE id = ?",
                             args=(employee_id,), many=False)['data']
    if not res:
        return None
    return EmployeesOutput(id=res[0], firstname=res[1], lastname=res[2], job=res[3], phone=res[4])


def add_employee(new_employee: EmployeesInput):
    res = base_manager.execute("INSERT INTO employees(firstname, lastname, job, phone)"
                               "VALUES (?, ?, ?, ?)"
                               "RETURNING id", args=(new_employee.firstname, new_employee.lastname, new_employee.job, new_employee.phone))
    return res


def update_employee(employee_id: int, employee: EmployeesInput):
    res = base_manager.execute("UPDATE employees SET firstname=?, lastname=?, job=?, phone=? WHERE id=? RETURNING id ",
                             args=(employee.firstname, employee.lastname, employee.job, employee.phone, employee_id, ))
    return res['data'][0][0]


def delete_employee(employee_id: int):
    res = base_manager.execute("DELETE FROM employees WHERE id=? RETURNING id ",
                             args=(employee_id,))
    return res['data'][0][0]
