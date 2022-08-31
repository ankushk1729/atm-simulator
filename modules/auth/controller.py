import maskpass
from modules.account.controller import AccountController
from modules.account.service import AccountService
from modules.auth.service import AuthService
from modules.user.schema import SchemaError, user_signup_schema
from modules.user.service import UserService
from schema import Schema, SchemaError
from utils.util import Util


class AuthController:

    def __init__(self):
        self.util = Util()
        self.user_service = UserService()
        self.account_controller = AccountController(())
        

    def login(self):
        auth_service = AuthService()
        try:
            while True:
                email = input('Enter your email : ')
                password = maskpass.askpass('Enter your password : ')
                user_info = auth_service.login(email, password)
                if  user_info :
                    break
                else : print('Invalid credentials')
            return user_info
        except :
            print('Unable to login')

    def signup(self):
        try:
            is_user_exists = True
            aadhar = 0
            while is_user_exists:
                aadhar = input('Enter your aadhar number : ')
                try:
                    if not aadhar.isdigit() : raise TypeError('Invalid input, please enter a number')
                    Schema(lambda n : len(str(n)) == 12, error = 'Aadhar should be of 12 digits').validate(aadhar)
                except TypeError as error:
                    print(str(error))
                    continue
                except SchemaError as error:
                    print(str(error))
                    continue
                
                if self.user_service.check_user_exists('aadhar', aadhar):
                    print('User with this aadhar already exists')
                else :
                    is_user_exists = False

            is_signup_schema_correct = False


            while not is_signup_schema_correct:
                try: 
                    full_name = input('Enter your full name : ')
                    email = input('Enter your email : ')
                    password = maskpass.askpass('Enter password : ')
                    phone = input('Enter your phone : ')
                    DOB = input('Enter your DOB in format DD-MM-YYYY : ')
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
            
            account_service = AccountService()
            account_type_id = account_service.get_account_type_id_by_name(name_to_key_mapping[int(choice)])
            self.create_approval_request(aadhar, account_type_id)
            print('Successfull signup')
            return (user_id, aadhar, account_type_id, name_to_key_mapping[int(choice)])

        except:
            print('Unable to create account')

    def create_user(self):
        (user_id, aadhar, account_type_id, account_name) = self.signup()
        self.user_service.approve_user('aadhar', aadhar)
        self.account_controller.create_account(aadhar, account_type_id, account_name)
        self.user_service.mark_request_as_approved_with_aadhar(aadhar)
    
    def create_approval_request(self, user_aadhar, account_type):
        self.user_service.create_approval_req(user_aadhar, account_type)

