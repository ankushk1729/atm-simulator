from config.data import admin_operations, admin_tasks_to_function_mapping
from modules.account.controller import AccountController
from modules.auth.controller import AuthController
from modules.transaction.controller import TransactionController
from modules.user.controller import UserController


class AdminMenu:
    def __init__(self, user_info):
        print('Welcome {}, '.format(user_info[1]))
        self.user_info = user_info
        self.user_controller = UserController(user_info, {})
        self.auth_controller = AuthController()
        self.account_controller = AccountController(user_info)
        self.transaction_controller = TransactionController(user_info)
        self.show_options()

    def show_options(self):
        while True:
            print('****************************************************')
            for i in range(0, len(admin_operations)):
                operation_text = admin_tasks_to_function_mapping[admin_operations[i]]
                print('Select {} to {}'.format(i + 1, operation_text))
            print('Select 0 to exit')
            print('****************************************************')

            try:
                choice = input()
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if int(choice) == 0:
                    break

                if not (int(choice) >= 0 and int(choice) <= 10) : raise ValueError('Please enter a number between 0 and 10')
            except ValueError as error:
                print(str(error))
                continue
            except TypeError as error:
                print(str(error))
                continue

            choice = int(choice)
            
            match choice:
                case 1:
                    self.user_controller.search_users_by_name()
                case 2:
                    self.user_controller.approve_user()
                case 3:
                    self.account_controller.create_account_handler()
                case 4:
                    self.auth_controller.create_user()
                case 5:
                    self.user_controller.delete_user()
                case 6:
                    self.user_controller.get_all_users()
                case 7:
                    self.transaction_controller.get_all_txns()
                case 8:
                    self.account_controller.get_all_accounts()
                case 9:
                    self.transaction_controller.get_user_txns()
                case 10:
                    self.user_controller.get_all_admins()
                case 0:
                    return
