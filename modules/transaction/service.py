
from utils.util import Util


class TransactionService:
    def __init__(self) :
        self.util = Util()
        self.root = self.util.get_query_root()

    def get_all_txns(self):
        get_txns_query = self.root[19].text

        cursor = self.util.execute_query(get_txns_query)

        if cursor == None:
            return []
        
        txns_list = list(cursor)
        cursor.close()
        return txns_list

    def get_account_transactions(self, account_num):
        get_account_transactions_query = self.root[21].text.format(account_num)

        cursor = self.util.execute_query(get_account_transactions_query)
        if cursor == None:
            return []
        
        txn_list = list(cursor)

        cursor.close()

        return txn_list

    def get_txn_id_from_name(self, name):
        get_txn_id_query = self.root[25].text.format(name)
        cursor = self.util.execute_query(get_txn_id_query)
        if cursor == None:
            return None

        txn_list = list(cursor)
        if len(txn_list) < 1: return None
        txn = txn_list[0][0]
        cursor.close()
        return txn

    def create_txn(self, balance, account_num, txn_name):
        txn_type = self.get_txn_id_from_name(txn_name)
        if txn_type == None:
            print('Unable to perform the transaction')
            return
        
        create_txn_query = self.root[24].text.format(balance, account_num, txn_type)
        cursor = self.util.execute_query_with_commit(create_txn_query)

        cursor.close()

