from server.database.db_manager import base_manager
from server.ostatki.models import OstatkiOutput, OstatkiInput


def get_ostatki():
    res = base_manager.execute("SELECT id, id_medicine, quantity FROM ostatki", many=True)
    print(res)
    ostatkis = []
    if not res:
        return None
    for ostatki in res['data']:
        ostatkis.append(OstatkiOutput(id=ostatki[0], id_medicine=ostatki[1], quantity=ostatki[2]))
    return ostatkis


def get_current_ostatki(ostatok_id: int):
    res = base_manager.execute("SELECT id, id_medicine, quantity, FROM ostatki WHERE id = ?",
                             args=(ostatok_id,), many=False)['data']
    if not res:
        return None
    return OstatkiOutput(id=res[0], id_medicine=res[1], quantity=res[2])


def add_ostatki(new_ostatok: OstatkiInput):
    res = base_manager.execute("INSERT INTO ostatki(id_medicine, quantity) "
                             "VALUES (?, ?) "
                             "RETURNING id ", args=(new_ostatok.id_medicine, new_ostatok.quantity))
    return res


def update_ostatki(ostatok_id: int, ostatki: OstatkiInput):
    res = base_manager.execute("UPDATE ostatki SET id_medicine=?, quantity=? WHERE id=? RETURNING id ",
                             args=(ostatki.id_medicine, ostatki.quantity, ostatok_id, ))
    return res['data'][0][0]


def delete_ostatki(ostatok_id: int):
    res = base_manager.execute("DELETE FROM ostatki WHERE id=? RETURNING id ",
                             args=(ostatok_id,))
    return res['data'][0][0]
