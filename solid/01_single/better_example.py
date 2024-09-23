import json
import sqlite3

class JsonParser:
    def parse(self, json_data: str) -> dict:
        ## Tout plein de trucs (s'il manque un champ...)
        return json.loads(json_data)

class DatabaseSaver:
    def save(self, data: dict) -> None:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (data['name'], data['age']))
        conn.commit()
        conn.close()

