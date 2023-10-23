from server.database.db_manager import base_manager
from server.clients.models import ClientsOutput, ClientsInput


def get_client():
    res = base_manager.execute("SELECT id, firstname, lastname, address, phone FROM clients", many=True)
    print(res)
    clients = []
    if not res:
        return None
    for client in res['data']:
        clients.append(ClientsOutput(id=client[0], firstname=client[1], lastname=client[2], address=client[3], phone=client[4]))
    return clients


def get_current_client(client_id: int):
    res = base_manager.execute("SELECT id, firstname, lastname, address, phone FROM clients WHERE id = ?",
                             args=(client_id,), many=False)['data']
    if not res:
        return None
    return ClientsOutput(id=res[0], firstname=res[1], lastname=res[2], address=res[3], phone=res[4])


def add_client(new_client: ClientsInput):
    res = base_manager.execute("INSERT INTO clients(firstname, lastname, address, phone)"
                             "VALUES (?, ?, ?, ?)"
                             "RETURNING id", args=(new_client.firstname, new_client.lastname, new_client.address, new_client.phone))
    return res


def update_client(client_id: int, clients: ClientsInput):
    res = base_manager.execute("UPDATE clients SET firstname=?, lastname=?, address=?, phone=?  WHERE id=? RETURNING id ",
                             args=(clients.firstname, clients.lastname, clients.address, clients.phone, client_id, ))
    return res['data'][0][0]


def delete_client(client_id: int):
    res = base_manager.execute("DELETE FROM clients WHERE id=? RETURNING id ",
                             args=(client_id,))
    return res['data'][0][0]
