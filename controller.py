from vehicle import Vehicle




class Controller:

    @classmethod
    def find_all_by_username(cls, username):
        result = c.execute("SELECT * FROM VEHICLE WHERE OWNER=username")
        return cls.build_vehicle(result)

    @classmethod
    def build_vehicle(cls, row):
        return Vehicle(row)

    @classmethod
    def create_user(cls, *params):
    	return User(params).save_to_db()


print(VehicleController.find_all_by_username('boby'))
