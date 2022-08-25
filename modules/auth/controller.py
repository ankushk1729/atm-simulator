from modules.auth.service import AuthService
from modules.user.schema import SchemaError, user_schema
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

    def login():
        pass
        # cnx = connection_obj.getInstance()
        # cursor = cnx.cursor()
        # cursor.execute('SELECT * from role')
        # for data in cursor:
        #     print(data)

    def signup(self):

        aadhar = int(input('Enter your aadhar number'))
        user_service  = UserService()
        is_user_exists = True
        while not is_user_exists:
            if user_service.check_user_exists(aadhar):
                print('User with this aadhar already exists')
            else :
                is_user_exists = False

        full_name = input('Enter your full name')
        email = input('Enter your email')
        password = input('Enter your pasword')
        phone = input('Enter your phone')
        # DOB = input('Enter your DOB in format DD/MM/YY')

        schema = {'full_name' : full_name, 'email' : email, 'phone': phone, 'aadhar': aadhar, 'password' : password}

        while True:
            try: 
                user_schema.validate(schema)
                break
            except SchemaError as error: 
                print(str(error))

        
        auth_service = AuthService()

        auth_service.signup(schema)

