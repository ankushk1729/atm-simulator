
from modules.account.controller import AccountController
from modules.auth.controller import *
from modules.user.service import UserService
from prettytable import PrettyTable


class UserController:

    def __init__(self, user_info, account_controller = None):
        self.user_service = UserService()
        if not account_controller == None : self.account_controller = account_controller
        self.user_info = user_info
    
    def create_user(self):
        auth_controller = AuthController()

        (user_id, aadhar) = auth_controller.signup()
        self.approve_user_by_unique_key('id', str(user_id))

    def approve_user(self):

        pending_users = self.show_pending_users()
        if len(pending_users) < 1: return
        while True:

            for i, val in enumerate(pending_users):
                print('{} aadhar - {}, id - {}'.format(i+1, val[1], val[0]))
            try:
                print('Select the user name from given list : ')
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
        self.user_service.approve_user('aadhar', requested_user[1])

        account_controller.create_account(requested_user[1], requested_user[2])

        self.user_service.mark_request_as_approved(requested_user[0])


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

        user = self.user_service.get_user(self.user_info[3])
    
        user_list = [user]
        user_table = PrettyTable()
        user_table.field_names = ['full_name', 'aadhar', 'email', 'phone']
        for user in user_list:
            user_table.add_row((user[1], user[3], user[7], user[6]))

        print(user_table)

        return user


    def show_pending_users(self):
        print('Pending user approvals : ')
        pending_users = self.user_service.get_pending_users()
        pending_users_table = PrettyTable()
        pending_users_table.field_names = ['data id', 'aadhar']
        for user in pending_users:
            pending_users_table.add_row((user[0], user[1]))

        print(pending_users_table)

        return pending_users


    def get_all_users(self):
        all_users = self.user_service.get_all_users()
        print('all users', all_users)
        all_users_table = PrettyTable()
        all_users_table.field_names = ['Id','Full Name', 'Aadhar', 'Email', 'Phone']
        for user in all_users:
            all_users_table.add_row(user)

        print('\nHere are all the users')
        print(all_users_table)


    def delete_user():
        pass

    def create_approval_request(self, user_aadhar, account_type):
        self.user_service.create_approval_req(user_aadhar, account_type)
