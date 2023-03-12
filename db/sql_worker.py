from classes import Export

import sqlite3 as sql


class Database:
    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()

    def vehicle_exists(self, site_name: str, vehicle_id: int) -> bool:
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM {site_name} WHERE vehicle_id = ?', (vehicle_id,)).fetchall()
            return bool(len(result))

    def add_vehicle(self, export: Export):
        with self.connection:
            self.cursor.execute(f'INSERT INTO {export.site_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (export.vehicle_id, export.link, export.title, export.photos, export.price, export.info, export.location, export.site_name, export.year, export.transmission))

    def get_vehicle(self, site_name: str, vehicle_id: int) -> Export:
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM {site_name} WHERE vehicle_id = ?', (vehicle_id,)).fetchone()
            return Export(*result)
