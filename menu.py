from controller import Controller
import sys


class Menu:
    controller = Controller()
    ask_for_command = """You can choose from the following commands:\nlist_all_free_hours\nlist_free_hours <date>\nsave_repair_hour <hour_id>\nupdate_repair_hour <hour_id>\ndelete_repair_hour <hour_id>\nadd_vehicle\nupdate_vehicle <vehicle_id>\ndelete_vehicle <vehicle_id>\nexit
                    """

    @classmethod
    def start(self):
        user_name = input('Hello!\nProvide your user_name:\n>>> ')
        # user = get_user_by_user_name(user_name)
        user = self.controller.check_if_user_exists(user_name)
        if user:
            print('Hello {}'.format(user))
            print(self.ask_for_command)

            while True:
                command = input('command> :')
                if command == 'list_all_free_hours':
                    self.controller.list_all_free_hours()

                if command == 'list_free_hours <date>':
                    date = input('please choose date: ')
                    self.controller.get_free_hours_by_date(date)

                if command == "save_repair_hour <hour_id>":
                    print('Your cars')
                    self.controller.list_vehicle_by_username(user_name)
                    vehicle = input('choose vehicle id')
                    print('Available services')
                    self.controller.list_services()
                    service = input('Choose service')

                if command == 'add_vehicle':
                    category = input('What is the category of your vehicle: ')
                    make = input('make: ')
                    model = input('model: ')
                    reg_number = input('register number: ')
                    gear_box = input('gear box: ')
                    owner = self.controller.get_id_of_username(user_name)
                    self.controller.add_vehicle(
                        category,
                        make,
                        model,
                        reg_number,
                        gear_box,
                        owner
                        )
                    print('Thank you! You added new personal vehicle!')
                if command == 'exit':
                    sys.exit()

        else:
            print('Unknown user!\n Would you like to create new user?')
            create_new = input('>>> ')
            if create_new.lower() in ['y', 'yes']:
                user_type = input('Are you a Client or Mechanic?\n>>> ')
                if len(user_type) == 0:
                    print('Invalid user type!')
                    sys.exit()
                new_user_name = input('Provide user_name:\n>>> ')
                if len(new_user_name) == 0:
                    print('Invalid user name!')
                    sys.exit()
                new_phone_number = input("Provide phone_number:\n>>>")
                if len(new_phone_number) == 0:
                    print('Invalid phone number!')
                    sys.exit()
                new_email = input("Provide email:\n>>>")
                if len(new_email) == 0:
                    print('Invalid email!')
                    sys.exit()
                new_address = input("Provide address:\n>>>")
                if len(new_address) == 0:
                    print('Invalid address!')
                    sys.exit()
                if user_type == 'Client':
                    self.controller.create_user(
                        new_user_name,
                        new_phone_number,
                        new_email,
                        new_address,
                        )
                    print('Thank you,{}\n !Welcome to Vehicle Services!\nNext time you try to login, provide your user_name!'.format(new_user_name))
                    print(self.ask_for_command)
                    command = input('command> :')
                elif user_type == 'Mechanic':
                    self.controller.create_mechanic(
                        new_user_name,
                        new_phone_number,
                        new_email,
                        new_address,
                        )
                    print('Thank you,{}!\nWelcome to Vehicle Services!\nNext time you try to login, provide your user_name!'.format(new_user_name))
            else:
                sys.exit()

if __name__=='__main__':
    Menu.start()
