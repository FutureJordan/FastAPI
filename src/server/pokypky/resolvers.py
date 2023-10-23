from server.database.db_manager import base_manager
from server.pokypky.models import PokupkyOutput, PokupkyInput


def get_pokupky():
    res = base_manager.execute("SELECT id, id_client, id_medicine, pokupka_date FROM pokupky", many=True)
    print(res)
    pokupki = []
    if not res:
        return None
    for pokupka in res['data']:
        pokupki.append(PokupkyOutput(id=pokupka[0], id_client=pokupka[1], id_medicine=pokupka[2], pokupka_date=pokupka[3]))
    return pokupki


def get_current_pokypky(pokupka_id: int):
    res = base_manager.execute("SELECT id, id_client, id_medicine, pokupka_date FROM pokypky WHERE id = ?",
                             args=(pokupka_id,), many=False)['data']
    if not res:
        return None
    return PokupkyOutput(id=res[0], id_client=res[1], id_medicine=res[2], pokupka_date=res[3])


def add_pokupky(new_pokupka: PokupkyInput):
    res = base_manager.execute("INSERT INTO pokupky(id_client, id_medicine, pokupka_date) "
                             "VALUES (?, ?, ?) "
                             "RETURNING id ", args=(new_pokupka.id_client, new_pokupka.id_medicine, new_pokupka.pokupka_date))
    return res


def update_pokupky(pokupka_id: int, pokupky: PokupkyInput):
    res = base_manager.execute("UPDATE pokupky SET id_client=?, id_medicine=?, pokupka_date=? WHERE id=? RETURNING id ",
                             args=(pokupky.id_client, pokupky.id_medicine, pokupky.pokupka_date, pokupka_id, ))
    return res['data'][0][0]


def delete_pokupky(pokupli_id: int):
    res = base_manager.execute("DELETE FROM pokupky WHERE id=? RETURNING id ",
                             args=(pokupli_id,))
    return res['data'][0][0]
