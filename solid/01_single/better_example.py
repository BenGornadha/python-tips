import json
import sqlite3


class JsonParser:
    def parse(self, json_data: str) -> dict:
        ## Tout plein de trucs (s'il manque un champ...)
        return json.loads(json_data)


class DatabaseSaver:

    def __init__(self) -> None:
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def save(self, data: dict) -> None:
        self.cursor.execute(f"INSERT INTO users (name, age) "
                            f"      VALUES (?, ?)",
                            (data['name'], data['age']))
        self.conn.commit()
        self._close_connection()

    def _close_connection(self) -> None:
        self.conn.close()
