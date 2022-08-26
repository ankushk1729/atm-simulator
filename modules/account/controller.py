from modules.account.service import AccountService


class AccountController:
    def __init__(self, user_info):
        self.user_info = user_info
        # self.account_num = account_num
        self.account_service = AccountService(user_info)

    def create_account(self, user_aadhar):
        
        account_type_id = self.get_account_selection()
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

