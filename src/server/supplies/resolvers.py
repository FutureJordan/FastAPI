from server.database.db_manager import base_manager
from server.supplies.models import SuppliesOutput, SuppliesInput


def get_supplies():
    res = base_manager.execute("SELECT id, id_supply, id_medicine, quantity FROM supplies", many=True)
    print(res)
    supplies = []
    if not res:
        return None
    for supplie in res['data']:
        supplies.append(SuppliesOutput(id=supplie[0], id_supply=supplie[1], id_medicine=supplie[2], quantity=supplie[3]))
    return supplies


def get_current_supplies(supplies_id: int):
    res = base_manager.execute("SELECT id, id_supply, id_medicine FROM supplies WHERE id = ?",
                             args=(supplies_id,), many=False)['data']
    if not res:
        return None
    return SuppliesOutput(id=res[0], id_supply=res[1], id_medicine=res[2], quantity=res[3])


def add_supplies(new_supplies: SuppliesInput):
    res = base_manager.execute("INSERT INTO supplies(id_supply, id_medicine, quantity)"
                             "VALUES (?, ?, ?)"
                             "RETURNING id", args=(new_supplies.id_supply, new_supplies.id_medicine, new_supplies.quantity))
    return res


def update_supplies(supplies_id: int, supplies: SuppliesInput):
    res = base_manager.execute("UPDATE supplies SET id_supply=?, id_medicine=?, quantity=? WHERE id=? RETURNING id ",
                             args=(supplies.id_supply, supplies.id_medicine, supplies.quantity, supplies_id, ))
    return res['data'][0][0]


def delete_supplies(supplies_id: int):
    res = base_manager.execute("DELETE FROM supplies WHERE id=? RETURNING id ",
                             args=(supplies_id,))
    return res['data'][0][0]
