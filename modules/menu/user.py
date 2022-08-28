from config.data import user_operations, user_tasks_to_function_mapping
from modules.account.controller import AccountController
from modules.transaction.controller import TransactionController
from modules.user.controller import UserController


class UserMenu:
    def __init__(self, user_info):
        self.user_info = user_info
        self.user_controller = UserController(user_info, {})
        self.account_controller = AccountController(user_info)
        self.transaction_controller = TransactionController(user_info)
        if self.user_controller.check_user_approved() :
            self.show_options()
        else : print('\n----- You are not yet approved by admin, please try again later -----\n')

    def show_options(self):

        print('Welcome {}, '.format(self.user_info[1]))
        while True:
            for i in range(0, len(user_operations)):
                operation_text = user_tasks_to_function_mapping[user_operations[i]]
                print('Select {} to {}'.format(i + 1, operation_text))
            print('Select 0 to exit')

            try:
                choice = input()
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if int(choice) == 0:
                    break
                if not (int(choice) >= 1 and int(choice) <= 5) : raise ValueError('Please enter a number between 0 and 5')
            except ValueError as error:
                print(str(error))
                continue
            except TypeError as error:
                print(str(error))
                continue

            choice = int(choice)
            
            match choice:
                case 1:
                    self.user_controller.get_current_user_data()
                case 2:
                    self.account_controller.get_balance()
                case 3:
                    self.transaction_controller.get_current_user_txns()
                case 4:
                    self.transaction_controller.withdraw()
                case 5:
                    self.transaction_controller.deposit()
                case 0:
                    return
