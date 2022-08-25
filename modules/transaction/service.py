from sqlite3 import Cursor
from utils.connect import connection_obj
class TransactionService:
    def __init__(self):
        self.connection_instance = connection_obj.getInstance()

    def get_transaction_id(self,txn_name):
        get_transactionid_query="select id from transaction-type where name='{}'".format(txn_name)
        cursor=self.connection_instance.cursor()
        cursor.execute(get_transactionid_query)
        transaction_ids=list(cursor)
        return transaction_ids[0]

    def create_transaction(self, txn_name, amount, account_num):
        txn_type=self.get_transaction_id(txn_name)
        create_transaction_query="insert into transaction(txn_type,amount,account_num) values('{}',{},{})".format( txn_type, amount, account_num)
        cursor=self.connection_instance.cursor()
        cursor.execute(create_transaction_query)

    def get_alltransac(self):
        query="select *from transaction"
        cursor=self.execute_query(query)
        return list(cursor)

        