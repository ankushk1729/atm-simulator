from sqlite3 import Cursor
from utils.connect import connection_obj
class AccountService():
    def __init__(self):
        self.connection_instance = connection_obj.getInstance()

    def execute_query(self,query):
        cursor=connection_obj.cursor()
        cursor.execute(query)
        self.connection_instance.commit()
        return cursor

    
    def get_balance(self,current_userid):
        query="select balance from account where user_id={}".format(current_userid)
        cursor=self.execute_query(query)
        return list(cursor[0])

    def update_balance(self,updated_balance):
        query="update account set balance={}".format(updated_balance)
        cursor=self.execute_query(query)
        
    def get_acctype(self, current_userid):
        query="select account_type from account where id={}".format(current_userid) #************
        cursor=self.execute_query(query)
        
    def get_acc_properties(self):
        query="select min_balance,max_withdrawal_amount from account-type where id={}".format(self.current_userid)
        cursor=self.execute_query(query)
        return list(cursor)[0]

    