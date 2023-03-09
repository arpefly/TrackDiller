from classes import Export

import sqlite3 as sql


class Database:
    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()

    def vehicle_exists(self, site_name: str, vehicle_id: str) -> bool:
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM {site_name} WHERE vehicle_id = ?', (vehicle_id,)).fetchall()
            return bool(len(result))

    def add_vehicle(self, site_name: str, export: Export):
        with self.connection:
            self.cursor.execute(f'INSERT INTO otomoto VALUES (?, ?, ?, ?, ?, ?, ?)', (export.vehicle_id, export.link, export.title, export.picture, export.price, export.info, export.location))

    def get_vehicle(self, site_name: str, vehicle_id: int):
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM {site_name} WHERE vehicle_id = ?', (vehicle_id,)).fetchmany(1)
            return result
