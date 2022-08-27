from modules.account.service import AccountService
from modules.auth.service import AuthService
from modules.user.schema import SchemaError, user_signup_schema
from modules.user.service import UserService
from utils.util import Util


class AuthController:

    def __init__(self):
        self.util = Util()
        self.user_service = UserService()
        

    def login(self):
        auth_service = AuthService()
        
        while True:
            email = input('Enter your email : ')
            password = input('Enter your password : ')
            user_info = auth_service.login(email, password)
            if  user_info :
                break
            else : print('Invalid credentials')

        return user_info

    def signup(self):

        user_service  = UserService()
        is_user_exists = True
        aadhar = 0
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

        user_id = auth_service.signup(schema)

        name_to_key_mapping = {1: 'savings', 2: 'current'}
        print('Please specify the type of account you want to open')
        while True:

            print('Enter 1 to open savings account')
            print('Enter 2 to open current account')
            print('Enter 0 to exit')
            try:
                choice = input()
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if int(choice) == 0:
                    return 0
                if not (int(choice) >= 0 and int(choice) <= 2) : raise ValueError('Please enter a number between 0 and 2')

                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))
        
        account_service = AccountService(schema)
        account_type_id = account_service.get_account_type_id_by_name(name_to_key_mapping[int(choice)])
        self.create_approval_request(aadhar, account_type_id)

        return (user_id, aadhar)

    def create_user(self):
        (user_id, aadhar) = self.signup()
        self.user_service.approve_user('id', str(user_id))
    
    def create_approval_request(self, user_aadhar, account_type):
        self.user_service.create_approval_req(user_aadhar, account_type)

