from server.database.db_manager import base_manager
from server.sclad.models import ScladOutput, ScladInput


def get_sclad():
    res = base_manager.execute("SELECT id, id_medicine, quantity FROM sclad", many=True)
    print(res)
    sclads = []
    if not res:
        return None
    for sclad in res['data']:
        sclads.append(ScladOutput(id=sclad[0], id_medicine=sclad[1], quantity=sclad[2]))
    return sclads


def get_current_sclad(sclad_id: int):
    res = base_manager.execute("SELECT id, id_medicine, quantity, FROM sclad WHERE id = ?",
                             args=(sclad_id,), many=False)['data']
    if not res:
        return None
    return ScladOutput(id=res[0], id_medicine=res[1], quantity=res[2])


def add_sclads(new_sclad: ScladInput):
    res = base_manager.execute("INSERT INTO sclad(id_medicine, quantity) "
                             "VALUES (?, ?) "
                             "RETURNING id ", args=(new_sclad.id_medicine, new_sclad.quantity))
    return res


def update_sclad(sclad_id: int, sclad: ScladInput):
    res = base_manager.execute("UPDATE sclad SET id_medicine=?, quantity=? WHERE id=? RETURNING id ",
                             args=(sclad.id_medicine, sclad.quantity, sclad_id, ))
    return res['data'][0][0]


def delete_sclad(sclad_id: int):
    res = base_manager.execute("DELETE FROM sclad WHERE id=? RETURNING id ",
                             args=(sclad_id,))
    return res['data'][0][0]
