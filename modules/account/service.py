from utils.util import Util


class AccountService:
    
    def __init__(self, user_info):
        self.user_info = user_info
        self.util = Util()
        self.root = self.util.get_query_root()

    def create_account(self, user_aadhar, account_type):
        create_acc_query = self.root[12].text.format(account_type, user_aadhar)
        cursor = self.util.execute_query_with_commit(create_acc_query)

        cursor.close()

    def get_account_type_id_by_name(self, account_name):

        get_account_id_query = self.root[13].text.format(account_name)

        cursor = self.util.execute_query(get_account_id_query)

        query_list = list(cursor)
        # print(query_list)
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

        if len(list(cursor)) > 0 : 
            return True


        cursor.close()

        return False
