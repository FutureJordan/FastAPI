from server.database.db_manager import base_manager
from server.administrator.models import AdminOutput, AdminInput

def get_admin():
    res = base_manager.execute("SELECT id, firstname, lastname, phone FROM admin", many=True)
    print(res)
    admins = []
    if not res:
        return None
    for admin in res['data']:
        admins.append(AdminOutput(id=admin[0], firstname=admin[1], lastname=admin[2], phone=admin[3]))
    return admins


def get_current_admin(admin_id: int):
    res = base_manager.execute("SELECT id, firstname, lastname, phone FROM admin WHERE id = ?",
                             args=(admin_id,), many=False)['data']
    if not res:
        return None
    return AdminOutput(id=res[0], firstname=res[1], lastname=res[2], phone=[3])


def add_admin(new_admin: AdminInput):
    res = base_manager.execute("INSERT INTO admin(firstname, lastname, phone)"
                             "VALUES (?, ?, ?)"
                             "RETURNING id", args=(new_admin.firstname, new_admin.lastname, new_admin.phone))
    return res


def update_admin(admin_id: int, admin: AdminInput):
    res = base_manager.execute("UPDATE admin SET firstname=?, lastname=?, phone=? WHERE id=? RETURNING id ",
                             args=(admin.firstname, admin.lastname, admin.phone, admin_id, ))
    return res['data'][0][0]


def delete_admin(admin_id: int):
    res = base_manager.execute("DELETE FROM admin WHERE id=? RETURNING id ",
                             args=(admin_id,))
    return res['data'][0][0]
