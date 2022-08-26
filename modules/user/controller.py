
from modules.account.controller import AccountController
from modules.auth.controller import *
from modules.user.service import UserService
from prettytable import PrettyTable


class UserController:

    def __init__(self, user_info):
        self.user_service = UserService()
        self.account_conrtoller = AccountController(user_info)
        self.user_info = user_info
    
    def create_user(self):
        auth_controller = AuthController()

        (user_id, aadhar) = auth_controller.signup()
        print(user_id)
        self.approve_user_by_unique_key('id', str(user_id))

    def approve_user(self):

        pending_users = self.show_pending_users()

        while True:

            for i, val in pending_users:
                print(i+1, 'aadhar - {}, id - {}'.format(val[2], val[0]))
            try:
                choice = input()
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if int(choice) == 0:
                    return 0
                if not (int(choice) >= 1 and int(choice) <= len(pending_users)) : raise ValueError('Please enter a number between the given range')

                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))

        choice = int(choice)
        requested_user = pending_users[choice - 1]
        self.user_service.approve_user('aadhar', requested_user[2])

        self.account_conrtoller.create_account(self.user_info[0])


    def search_users_by_name(self):
        name = input('Enter the name to search : ')

        user_search_list = self.user_service.search_users('full_name', name)

        user_search_table = PrettyTable()
        user_search_table.field_names = ['full_name', 'email', 'phone']
        for user in user_search_list:
            user_search_table.add_row(user)

        print('\nHere are the matching results')
        print(user_search_table)

    def get_current_user_data(self):

        print(self.user_info[3])

        user = self.user_service.get_user(self.user_info[3])

        if user == None:
            print('No user found with given aadhar')
            return None
        else : 
            # print(user)
            return user


    def show_pending_users(self):
        print('Pending user approvals : ')
        pending_users = self.user_service.get_pending_users()
        pending_users_table = PrettyTable()
        pending_users_table.field_names = ['data id', 'aadhar']
        for user in pending_users:
            pending_users_table.add_row(user)

        print(pending_users_table)

        return pending_users


    def get_all_users(self):
        self.user_service.get_all_users()

    def delete_user():
        pass

    def create_approval_request(self, user_aadhar, account_type):
        self.user_service.create_approval_req(user_aadhar, account_type)
