from user import User
from mechanic import Mechanic
from repair_hours import  RepairHour


class Controller:

    # @classmethod
    # def find_all_by_username(cls, username):
    #     result = .execute("SELECT * FROM VEHICLE WHERE OWNER=username")
    #     return cls.build_vehicle(result)
    #
    # @classmethod
    # def build_vehicle(cls, row):
    #     return Vehicle(row)

    @classmethod
    def create_user(cls, *params):
        return User(*params).save_to_db(*params)

    @classmethod
    def create_mechanic(cls, *params):
        return Mechanic(*params).save_to_db(*params)

    @classmethod
    def check_if_user_exists(cls, username):
        return User.check_user(username)

    @classmethod
    def list_all_free_hours(cls):
        return RepairHour.get_free_hours()

    @classmethod
    def get_free_hours_by_date(cls, date):
        return RepairHour.get_free_hours_date(date)





