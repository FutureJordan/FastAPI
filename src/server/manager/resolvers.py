from server.database.db_manager import base_manager
from server.manager.models import ManagerOutput, ManagerInput


def get_manager():
    res = base_manager.execute("SELECT id, firstname, lastname, phone FROM manager", many=True)
    print(res)
    managers = []
    if not res:
        return None
    for manager in res['data']:
        managers.append(ManagerOutput(id=manager[0], firstname=manager[1], lastname=manager[2], phone=manager[3]))
    return managers


def get_current_manager(manager_id: int):
    res = base_manager.execute("SELECT id, firstname, lastname, phone FROM manager WHERE id = ?",
                             args=(manager_id,), many=False)['data']
    if not res:
        return None
    return ManagerOutput(id=res[0], firstname=res[1], lastname=res[2], phone=res[3])


def add_manager(new_manager: ManagerInput):
    res = base_manager.execute("INSERT INTO manager(firstname, lastname, phone)"
                               "VALUES (?, ?, ?)"
                               "RETURNING id", args=(new_manager.firstname, new_manager.lastname, new_manager.phone))
    return res


def update_manager(manager_id: int, manager: ManagerInput):
    res = base_manager.execute("UPDATE manager SET firstname=?, lastname=?, phone=? WHERE id=? RETURNING id ",
                             args=(manager.firstname, manager.lastname, manager.phone, manager_id, ))
    return res['data'][0][0]


def delete_manager(manager_id: int):
    res = base_manager.execute("DELETE FROM manager WHERE id = ? RETURNING id ",
                             args=(manager_id,))
    return res['data'][0][0]