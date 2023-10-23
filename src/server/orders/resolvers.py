from server.database.db_manager import base_manager
from server.orders.models import OrdersOutput, OrdersInput


def get_order():
    res = base_manager.execute("SELECT id, id_client, order_date FROM orders", many=True)
    print(res)
    orders = []
    if not res:
        return None
    for order in res['data']:
        orders.append(OrdersOutput(id=order[0], id_client=order[1], order_date=order[2]))
    return orders


def get_current_orders(order_id: int):
    res = base_manager.execute("SELECT id, id_client, order_date, FROM orders WHERE id = ?",
                             args=(order_id,), many=False)['data']
    if not res:
        return None
    return OrdersOutput(id=res[0], id_client=res[1], order_date=res[2])


def add_order(new_order: OrdersInput):
    res = base_manager.execute("INSERT INTO orders(id_client, order_date) "
                             "VALUES (?, ?) "
                             "RETURNING id ", args=(new_order.id_client, new_order.order_date))
    return res


def update_order(order_id: int, orders: OrdersInput):
    res = base_manager.execute("UPDATE orders SET id_client=?, order_date=? WHERE id=? RETURNING id ",
                             args=(orders.id_client, orders.order_date, order_id, ))
    return res['data'][0][0]


def delete_orders(order_id: int):
    res = base_manager.execute("DELETE FROM orders WHERE id=? RETURNING id ",
                             args=(order_id,))
    return res['data'][0][0]
