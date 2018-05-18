from collections import namedtuple
import sqlite3
from prettytable import PrettyTable




DB_NAME = "vehicle_management.db"

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

class RepairHour:
    def __init__(self, date, start_hour, vehicle=None, bill=None, mechanic_service=None):
        self.date = date
        self.start_hour = start_hour
        self.vehicle = vehicle
        self.bill = bill
        self.mechanic_service = mechanic_service

    @classmethod
    def get_free_hours(cls):
        x = PrettyTable()
        x.field_names = ['date', 'start hour']
        for i in c.execute('SELECT id, date, start_hour FROM REPAIR_HOURS WHERE VEHICLE IS NULL'):
            x.add_row([i[0], i[1]])
        print(x)

    @classmethod
    def get_free_hours_date(cls, date):
        x = PrettyTable()
        x.field_names = ['date', 'start hour']
        for i in c.execute('SELECT id, date, start_hour FROM REPAIR_HOURS WHERE VEHICLE IS NULL AND DATE=?', (date,)):
            x.add_row([i[0], i[1]])
        print(x)

# print(RepairHour.get_free_hours_date('25-05-2018'))
