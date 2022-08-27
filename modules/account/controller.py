from modules.account.service import AccountService
from prettytable import PrettyTable


class AccountController:
    def __init__(self, user_info):
        self.user_info = user_info
        # self.account_num = account_num
        self.account_service = AccountService(user_info)


    def create_account_handler(self):
        while True:
            try:
                aadhar = input('Please enter the aadhar number of registered user')
                if not aadhar.isdigit() : raise TypeError('Invalid input, please enter a number')
                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))

        account_type_id = self.get_account_selection()
        if self.account_service.check_acc_type_exists_for_user(aadhar, account_type_id):
            print('This account type already exists for this user')
            return
        self.account_service.create_account(aadhar, account_type_id)

    def create_account(self, user_aadhar, account_type_id):
        
        # account_type_id = self.get_account_selection()
        self.account_service.create_account(user_aadhar, account_type_id)

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
            
        account_type_id = self.account_service.get_account_type_id_by_name(name_to_key_mapping[int(choice)])
        return account_type_id

    def get_balance(self):

        print('Please select the account : ')

        user_accounts = self.account_service.get_user_accounts(self.user_info[3])
        
        for i, user_acct in enumerate(user_accounts):
            print('{} Account number :{}, balance : {}'.format(i + 1,user_acct[0], user_acct[1]))


    def get_all_accounts(self):
        all_accounts = self.account_service.get_all_accounts()

        all_accounts_table = PrettyTable()
        all_accounts_table.field_names = ['Account number', 'balance', "User's aadhar", 'name']
        for account in all_accounts:
            all_accounts_table.add_row((account[0],account[1], account[3], account[7]))

        print('\nHere are all the accounts')
        print(all_accounts_table)
