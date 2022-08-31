
from datetime import datetime

from modules.account.controller import AccountController
from modules.auth.controller import *
from modules.user.service import UserService
from prettytable import PrettyTable


class UserController:

    def __init__(self, user_info, auth_controller):
        self.user_service = UserService()
        self.auth_controller = auth_controller
        self.account_controller = AccountController(user_info)
        self.account_service = AccountService()
        self.user_info = user_info
    
    

    def approve_user(self):

        try:
            pending_users = self.show_pending_users()
            if len(pending_users) < 1: return
            while True:
                try:
                    print('Select the user by S.no : ')
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
            account_name = self.account_service.get_account_name_by_id(requested_user[2])

            self.user_service.approve_user('aadhar', requested_user[1])

            self.account_controller.create_account(requested_user[1], requested_user[2], account_name)

            self.user_service.mark_request_as_approved(requested_user[0])

            print('\n----- User approved successfully -----\n')

        except :
            print('Unable to approve user')

    def search_users_by_name(self):

        try: 
            name = input('Enter the name to search : ')

            user_search_list = self.user_service.search_users('full_name', name)

            user_search_table = PrettyTable()
            user_search_table.field_names = ['full_name', 'email', 'phone']
            for user in user_search_list:
                user_search_table.add_row(user)

            print('\nHere are the matching results')
            print(user_search_table)

        except: 
            print('Unable to search users, please try again later')


    def get_age_from_dob(self, dob):
        try:
            date = datetime.strptime(dob, '%d-%m-%Y')
            age = round(((datetime.today() - date).days/365))
            return age
        except:
            return None

    def get_current_user_data(self):

        try:
            user = self.user_service.get_user(self.user_info[3])
            user_list = [user]
            
            dob = user[4]
            age = self.get_age_from_dob(dob)

            user_table = PrettyTable()
            user_table.field_names = ['full_name', 'aadhar', 'email', 'phone', 'age']
            for user in user_list:
                user_table.add_row((user[1], user[3], user[7], user[6], age))

            print(user_table)

            return user
        except: 
            return None

    def show_pending_users(self):
        try:
            print('Pending user approvals : ')
            pending_users = self.user_service.get_pending_users()
            pending_users_table = PrettyTable()
            pending_users_table.field_names = ['S.no', 'Request id', 'aadhar']
            for ind, user in enumerate(pending_users):
                pending_users_table.add_row((ind + 1, user[0], user[1]))

            print(pending_users_table)

            return pending_users
        except: 
            print('Unable to find pending users')
            return None

    def get_all_users(self):
        try:
            all_users = self.user_service.get_all_users()
            all_users_table = PrettyTable()
            all_users_table.field_names = ['Id','Full Name', 'Aadhar', 'Email', 'Phone']
            for user in all_users:
                all_users_table.add_row(user)

            print('\nHere are all the users')
            print(all_users_table)
        except:
            print('Unable to find all users')

    def check_user_approved(self):

        user_data = self.user_service.get_user(self.user_info[3])
        if user_data[5] == 1:
            return True
    
        return False

    def delete_user(self):
        while True:

            try:
                print('Enter the aadhar number to delete the user : ')
                aadhar_choice = input()
                if not aadhar_choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if int(aadhar_choice) == 0:
                    return 0
                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))

        try:
            aadhar = int(aadhar_choice)
            if not self.user_service.check_user_exists('aadhar', aadhar):
                print('\n-----No user with this aadhar -----\n')
                return
            self.user_service.delete_user(aadhar)
            print('\n------- Successfully deleted the user and linked accounts -------\n')
        except:
            print('Unable to delete the user')

    def get_all_admins(self):
        try:
            admins_list = self.user_service.get_all_admins()

            admins_table = PrettyTable()
            admins_table.field_names = ["Name", "Phone number", 'Created at']
            for admin in admins_list:
                admins_table.add_row(admin)

            print('\n ----- Here are all the admins -----')
            print(admins_table)
        except: 
            print('Unable to find all the admins')