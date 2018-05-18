import sqlite3
import constants
#from constants import insert_base_user

DB_NAME = "vehicle_management.db"

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

#
# insert_base_user = """
# INSERT INTO BASE_USER (user_name, email, phone_number, address)
#  VALUES (:user_name, :email, :phone_number, :address
#  )
# """

# c.execute(insert_base_user, {'user_name': 'dux',
#                              'email': 'dux@abv.bg',
#                              'phone_number': 121,
#                              'address': 'Ruse'})

class Mechanic:
    def __init__(self, user_name, email, phone_number, address):
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.address = address


    @classmethod
    def save_to_db(cls, username, email, phone_number, address):
        c.execute(constants.insert_base_user,
                  {'user_name': username,
                   'email': email,
                   'phone_number': phone_number,
                   'address': address})
        db.commit()
