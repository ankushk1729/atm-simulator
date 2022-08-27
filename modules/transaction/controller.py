
from modules.account.service import AccountService
from modules.transaction.service import TransactionService
from prettytable import PrettyTable


class TransactionController:
    
    def __init__(self, user_info):
        self.user_info = user_info
        self.transaction_service = TransactionService()
        self.account_service = AccountService(user_info)


    def get_all_txns(self):
        txns_list = self.transaction_service.get_all_txns()
        txn_table = PrettyTable()
        txn_table.field_names = ['Transaction id', 'Amount', 'Account num', 'Transaction Type']
        for txn in txns_list:
            txn_table.add_row((txn[0], txn[2], txn[3], txn[5]))

        print('\nHere are the transactions')
        print(txn_table)

    def get_user_txns(self):
        user_accounts = self.account_service.get_user_accounts(self.user_info[3])


        user_account_list = [x[0] for x in user_accounts]

        user_account_nums = tuple(user_account_list)

        


        print(user_account_nums)
        
    #pending
    def withdraw(self):

        user_accounts = self.account_service.get_user_accounts(self.user_info[3])
  
        while True:
  
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


        # account_info = self.account_service.get_account_info(account_num)

        pass

    def deposit():
        pass
