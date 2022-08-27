from modules.transaction.service import TransactionService
from prettytable import PrettyTable


class TransactionController:
    
    def __init__(self, user_info):
        self.user_info = user_info
        self.transaction_service = TransactionService()

    def get_all_txns(self):
        txns_list = self.transaction_service.get_all_txns()
        txn_table = PrettyTable()
        txn_table.field_names = ['Transaction id', 'Amount', 'User id']
        for txn in txns_list:
            txn_table.add_row(txn)

        print('\nHere are the transactions')
        print(txn_table)

    def get_user_txns():
        pass

    def withdraw():
        pass

    def deposit():
        pass
