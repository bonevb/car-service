import sqlite3
from constants import insert_base_user

DB_NAME = "vehicle_management.db"

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


class User:
    def __init__(self, user_name, email, phone_number, address):
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    @classmethod
    def create_user(self, username, email, phone_number, address):
        c.execute(insert_base_user,
                  {'user_name': username,
                   'email': email,
                   'phone_number': phone_number,
                   'address': address})

    def get_all_vehicle_by_username(self, username):
        pass
