import sqlite3
import os

from server import settings


class DBManager:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

    def check_base(self):
        return os.path.exists(self.db_path)

    def connect_to_base(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn, cur

    def create_base(self, script_path: str):
        conn, cur = self.connect_to_base()
        try:
            cur.executescript(open(script_path).read())
            conn.commit()
            conn.close()
        except Exception as ex:
            print(ex)

    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_to_base()
        try:
            res = cur.execute(query, args)
            if not res:
                return None
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            return {"code": 200, "data": result}
        except sqlite3.Error as er:
            print(str(er))
            return {'code': 500}
        finally:
            conn.close()


base_manager = DBManager(settings.DB_PATH)
# base_manager.create_base("C:\Project_pharmacy\src\server\database\\create_base.sql")

