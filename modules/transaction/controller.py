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
        

    def withdraw():
        pass

    def deposit():
        pass
