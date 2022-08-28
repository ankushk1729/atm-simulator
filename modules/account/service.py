from utils.util import Util


class AccountService:
    
    def __init__(self):
        self.util = Util()
        self.root = self.util.get_query_root()

    def create_account(self, user_aadhar, account_type, initial_balance):
        create_acc_query = self.root[12].text.format(account_type, user_aadhar, initial_balance)
        cursor = self.util.execute_query_with_commit(create_acc_query)

        cursor.close()

    def get_account_type_id_by_name(self, account_name):

        get_account_id_query = self.root[13].text.format(account_name)

        cursor = self.util.execute_query(get_account_id_query)

        query_list = list(cursor)
        cursor.close()
        if len(query_list) < 1 : 
            return None

        return query_list[0][0]


    def approve_requests(self):

        pending_requests_query = self.root[14].text

        self.util.execute_query(pending_requests_query)


    def get_user_accounts(self, user_aadhar):

        user_accounts_query = self.root[16].text.format(user_aadhar)

        cursor = self.util.execute_query(user_accounts_query)
        account_list = list(cursor)
        cursor.close()
        return account_list

    def check_acc_type_exists_for_user(self, aadhar, account_type):
        check_acc_type_exists_for_user_query = self.root[17].text.format(aadhar, account_type)

        cursor = self.util.execute_query(check_acc_type_exists_for_user_query)

        query_list = list(cursor)
        if len(query_list) > 0 : 
            return True


        cursor.close()
        return False

    def get_all_accounts(self):
        all_accounts_query = self.root[20].text

        cursor = self.util.execute_query(all_accounts_query)
        accounts_list = list(cursor)
        if cursor == None:
            return []

        cursor.close()

        return accounts_list

    def get_account_info(self, account_num):
        account_info_query = self.root[23].text.format(account_num)

        cursor = self.util.execute_query(account_info_query)

        if cursor == None:
            return None

        account_info_list = list(cursor)
        account_info = account_info_list[0]
        cursor.close()

        return account_info

        
    def update_balance(self, balance, account_num):

        update_balance_query = self.root[22].text.format(balance, account_num)

        cursor = self.util.execute_query_with_commit(update_balance_query)

        cursor.close()

    def get_account_name_by_id(self, account_type_id):
        account_name_query = self.root[26].text.format(account_type_id)

        cursor = self.util.execute_query(account_name_query)

        if cursor == None:
            return None
        
        account_name_list = list(cursor)

        if len(account_name_list) < 1:
            return None

        cursor.close()
        return account_name_list[0][0]
