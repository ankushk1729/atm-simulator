
from modules.auth.controller import AuthController
from modules.user.service import UserService
from prettytable import PrettyTable


class UserController:

    def __init__(self):
        self.user_service = UserService()
    
    def create_user(self):
        auth_controller = AuthController()

        (user_id, aadhar) = auth_controller.signup()
        print(user_id)
        self.approve_user_by_unique_key('id', str(user_id))

    def approve_user_by_unique_key(self, unique_field_key, unique_field_value):

        self.user_service.approve_user(unique_field_key, unique_field_value)

    def search_users_by_name(self):
        name = input('Enter the name to search : ')

        user_search_list = self.user_service.search_users('full_name', name)

        user_search_table = PrettyTable()
        user_search_table.field_names = ['full_name', 'email', 'phone']
        for user in user_search_list:
            user_search_table.add_row(user)

        print('\nHere are the matching results')
        print(user_search_table)

    def get_user_data(self, aadhar):

        user = self.user_service.get_user(aadhar)

        if user == None:
            print('No user found with given aadhar')
            return None
        else : 
            # print(user)
            return user


    def get_all_users(self):
        pass

