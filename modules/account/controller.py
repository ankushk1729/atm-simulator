from modules.account.service import AccountService
from modules.user.service import UserService
from prettytable import PrettyTable


class AccountController:
    def __init__(self, user_info):
        self.user_info = user_info
        self.account_service = AccountService()
        self.user_service = UserService()


    def create_account_handler(self):
        while True:
            try:
                aadhar = input('Please enter the aadhar number of registered user : ')
                if not aadhar.isdigit() : raise TypeError('Invalid input, please enter a number')
                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))
        aadhar = int(aadhar)

        try:
            if not self.user_service.check_user_exists('aadhar', aadhar):
                print('\n----- No user with aadhar {} ----- \n'.format(aadhar))
                return
            
            if not self.user_service.check_user_approved(aadhar):
                print('\nUser is not approved yet\n')
                return

            account_type_id = self.get_account_selection()
            account_name = self.account_service.get_account_name_by_id(account_type_id)
            if self.account_service.check_acc_type_exists_for_user(aadhar, account_type_id):
                print('\n-----  This account type already exists for this user ----- \n')
                return
            self.create_account(aadhar, account_type_id, account_name)
            print('Successfully created the account')
        except : 
            print('Unable to create account')


    def create_account(self, user_aadhar, account_type_id, account_name):
        try:
            initial_balance = 0
            if account_name == 'savings':
                initial_balance = 5000
            else: initial_balance = 10000

            self.account_service.create_account(user_aadhar, account_type_id, initial_balance)

        except :
            print('Unable to create account')

    def get_account_selection(self):
        name_to_key_mapping = {1: 'savings', 2: 'current'}
        while True:
            print('Enter 1 for savings account')
            print('Enter 2 for current account')
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

        try:    
            account_type_id = self.account_service.get_account_type_id_by_name(name_to_key_mapping[int(choice)])
            return account_type_id

        except : 
            return None

    def get_balance(self):

        try:
            user_accounts = self.account_service.get_user_accounts(self.user_info[3])
            
            user_accounts_table = PrettyTable()
            user_accounts_table.field_names = ['Account number', 'balance']
            for account in user_accounts:
                user_accounts_table.add_row((account[0],account[1]))

            print('\n----- Here are all your accounts -----\n')
            print(user_accounts_table)

        except :
            print('Unable to fetch balance')

    def get_all_accounts(self):
        try:
            all_accounts = self.account_service.get_all_accounts()

            all_accounts_table = PrettyTable()
            all_accounts_table.field_names = ['Account number', 'balance', "User's aadhar", 'Account type']
            for account in all_accounts:
                all_accounts_table.add_row((account[0],account[1], account[3], account[7]))

            print('\n----- Here are all the accounts -----\n')
            print(all_accounts_table)
        except : 
            print('Unable to fetch all the users')
