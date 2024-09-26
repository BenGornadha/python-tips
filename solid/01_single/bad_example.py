import json
import sqlite3

class DataHandler:
    def process_data(self, json_data: str) -> None:
        data = self._parse_json(json_data)
        self._save_to_db(data)

    def _parse_json(self, json_data: str) -> dict:
        ## Tout plein de trucs (s'il manque un champ, transformer un string en int...)
        return json.loads(json_data)

    def _save_to_db(self, data: dict) -> None:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (data['name'], data['age']))
        conn.commit()
        conn.close()