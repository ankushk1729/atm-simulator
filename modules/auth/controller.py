from modules.auth.service import AuthService
from modules.user.schema import Regex, SchemaError, user_signup_schema
from modules.user.service import UserService


class AuthController:

    def handler(self):
        while True:
            print('Enter 1 to Sign up')
            print('Enter 2 to Sign in')
            print('Enter 0 to exit')

            try:
                choice = input()
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if not (int(choice) >= 0 and int(choice) <= 2) : raise ValueError('Please enter a number between 0 and 2')
                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))


        choice = int(choice)
        match choice : 
            case 1: 
                self.signup()
            case 2:
                self.login()
            case 0:
                return 0

    def login(self):
        auth_service = AuthService()
        
        while True:
            email = input('Enter your email : ')
            password = input('Enter your password : ')
            user_info = auth_service.login(email, password)
            if  user_info :
                print(user_info)
                break
            else : print('Invalid credentials')

    def signup(self):

        user_service  = UserService()
        is_user_exists = True
        while is_user_exists:
            aadhar = input('Enter your aadhar number : ')
            try:
                if not aadhar.isdigit() : raise TypeError('Invalid input, please enter a number')
            except TypeError as error:
                print(str(error))
                continue

            if user_service.check_user_exists('aadhar', aadhar):
                print('User with this aadhar already exists')
            else :
                is_user_exists = False

        is_signup_schema_correct = False


        while not is_signup_schema_correct:
            try: 
                full_name = input('Enter your full name :')
                email = input('Enter your email : ')
                password = input('Enter your password : ')
                phone = int(input('Enter your phone : '))
                DOB = input('Enter your DOB in format DD-MM-YY : ')
                schema = {'full_name' : full_name, 'email' : email, 'phone': phone, 'aadhar': aadhar, 'password' : password, 'DOB': DOB}
                user_signup_schema.validate(schema)
                is_signup_schema_correct = True
            except SchemaError as error: 
                print(str(error))

        
        auth_service = AuthService()

        auth_service.signup(schema)

