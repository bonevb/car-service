from user import User
from mechanic import Mechanic
from repair_hours import  RepairHour
from vehicle import Vehicle
# from services import Service


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

    @classmethod
    def get_id_of_username(cls, username):
        return User.get_client_id(username)

    @classmethod
    def add_vehicle(cls, *params):
        return Vehicle(*params).save_vehicle_to_db(*params)

    @classmethod
    def list_vehicle_by_username(cls, username):
        user_name = User.get_client_id(username)
        return Vehicle.list_vehicle(user_name)

    @classmethod
    def list_services(cls):
        return Service.print_service()

    @classmethod
    def save_repair_hour(id, car_id, service_id):
        return RepairHour.save_repair_hour_by_id()

    @classmethod
    def update_vehicle(cls, id, *params):
        return Vehicle(*params).update_vehicle_in_db(id, *params)

    @classmethod
    def delete_vehicle(cls, id, owner):
        return Vehicle.remove_from_db(id, owner)



# Controller.list_vehicle_by_username('tedi')

# Controller.list_services()
