from server.database.db_manager import base_manager
from server.suppliers.models import SuppliersOutput, SuppliersInput


def get_supplier():
    res = base_manager.execute("SELECT id, title, address, phone FROM suppliers", many=True)
    print(res)
    suppliers = []
    if not res:
        return None
    for supplier in res['data']:
        suppliers.append(SuppliersOutput(id=supplier[0], title=supplier[1], address=supplier[2], phone=supplier[3]))
    return suppliers


def get_current_supplier(supplier_id: int):
    res = base_manager.execute("SELECT id, title, address, phone FROM suppliers WHERE id = ?",
                             args=(supplier_id,), many=False)['data']
    if not res:
        return None
    return SuppliersOutput(id=res[0], title=res[1], address=res[2], phone=[3])


def add_supplier(new_supplier: SuppliersInput):
    res = base_manager.execute("INSERT INTO suppliers(title, address, phone)"
                             "VALUES (?, ?, ?)"
                             "RETURNING id", args=(new_supplier.title, new_supplier.address, new_supplier.phone))
    return res


def update_supplier(supplier_id: int, supplier: SuppliersInput):
    res = base_manager.execute("UPDATE suppliers SET title=?, address=?, phone=? WHERE id=? RETURNING id ",
                             args=(supplier.title, supplier.address, supplier.phone, supplier_id, ))
    return res['data'][0][0]


def delete_supplier(supplier_id: int):
    res = base_manager.execute("DELETE FROM suppliers WHERE id=? RETURNING id ",
                             args=(supplier_id,))
    return res['data'][0][0]
