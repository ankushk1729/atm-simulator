from config.data import user_operations, user_tasks_to_function_mapping
from modules.user.controller import UserController


class UserMenu:
    def __init__(self, user_info):
        print('Welcome {}, '.format(user_info[1]))
        self.user_info = user_info
        self.user_controller = UserController(user_info)
        self.show_options()

    def show_options(self):

        while True:
            for i in range(0, len(user_operations)):
                operation_text = user_tasks_to_function_mapping[user_operations[i]][0]
                print('Select {} to {}'.format(i, operation_text))
            print('Select 5 to exit')

            try:
                choice = input()
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if not (int(choice) >= 0 and int(choice) <= 4) : raise ValueError('Please enter a number between 0 and 2')
                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))

        choice = int(choice)

        
        match choice:
            case 0:
                print(self.user_controller.get_current_user_data())
            case 1:
                self.user_controller.get_balance()
            case 2:
                self.user_controller.get_user_txns()
            case 3:
                self.user_controller.withdraw()
            case 4:
                self.user_controller.deposit()

