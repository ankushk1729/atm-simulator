import pyfiglet

from modules.auth.controller import AuthController
from modules.menu.admin import AdminMenu
from modules.menu.user import UserMenu
from utils.connect import connection_obj
from utils.util import Util


class Main():
    def __init__(self):
        self.auth_controller = AuthController()
        self.util = Util()
        self.handler()

    def handler(self):
        welcome_msg = pyfiglet.figlet_format('ATM SIMULATOR')
        print(welcome_msg)
        while True:
            print('Enter 1 to Sign up')
            print('Enter 2 to Sign in')
            print('Enter 0 to exit')

            try:
                choice = input()
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if not (int(choice) >= 0 and int(choice) <= 2) : raise ValueError('Please enter a number between 0 and 2')
            except ValueError as error:
                print(str(error))
                continue
            except TypeError as error:
                print(str(error))
                continue

            choice = int(choice)
            match choice : 
                case 1: 
                    self.auth_controller.signup()
                case 2:
                    user_info = self.auth_controller.login()
                    if self.util.authorize_permissions(user_info[0], 'admin'):
                        AdminMenu(user_info)
                    else :
                        UserMenu(user_info)
                case 0:
                    connection_obj.cnx.close()
                    goodbye_msg = pyfiglet.figlet_format('THANK YOU FOR VISITING!')
                    print(goodbye_msg)
                    exit() 


main = Main()

