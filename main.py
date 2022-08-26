from modules.auth.controller import AuthController


class Main():
    def __init__(self):
        self.auth_controller = AuthController()
        self.handler()

    def handler(self):
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
            except TypeError as error:
                print(str(error))

            choice = int(choice)
            match choice : 
                case 1: 
                    self.auth_controller.signup()
                case 2:
                    self.auth_controller.login()
                case 0:
                    exit() 

main = Main()

