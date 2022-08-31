from utils.util import Util


class UserService:

    def __init__(self):
        self.util = Util()
        self.root = self.util.get_query_root()

    def check_user_exists(self, param_key, param_value):
        query = self.root[11].text.format(param_key, param_value)
        cursor = self.util.execute_query(query)
        queryList = list(cursor)
        cursor.close()

        if len(queryList) < 1: return False
        return True

    def approve_user(self, unique_field_key, unique_field_value):
        if unique_field_key == 'id':
            approve_user_query = self.root[4].text.format(unique_field_key, unique_field_value)
            cursor = self.util.execute_query_with_commit(approve_user_query)
            cursor.close()

        elif unique_field_key == 'aadhar':
            approve_user_query = self.root[5].text.format(unique_field_key, unique_field_value)
            cursor = self.util.execute_query_with_commit(approve_user_query)
            cursor.close()

        

    def mark_request_as_approved(self, request_id):
        mark_req_as_approved = self.root[18].text.format(request_id)

        cursor = self.util.execute_query_with_commit(mark_req_as_approved)
        cursor.close()

        
    def mark_request_as_approved_with_aadhar(self, aadhar):
        mark_req_as_approved = self.root[28].text.format(aadhar)

        cursor = self.util.execute_query_with_commit(mark_req_as_approved)
        cursor.close()


    def search_users(self, search_key, search_value):

        search_user_query = self.root[6].text.format(search_value)
        

        
        cursor = self.util.execute_query(search_user_query)
    
        user_search_list = list(cursor)


        cursor.close()
        return user_search_list

    def get_user(self, aadhar):

        get_user_query = self.root[7].text.format(aadhar)

        cursor = self.util.execute_query(get_user_query)
        users_list = list(cursor)
        if len(users_list) < 1 : 
            return None

        user = users_list[0]
        cursor.close()
        return user

    def get_all_users(self):
        get_users_query = self.root[10].text
        cursor = self.util.execute_query(get_users_query)

        if cursor == None:
            return []
        
        users_list = list(cursor)
        return users_list

    def get_pending_users(self):
        pending_users_query = self.root[14].text

        cursor = self.util.execute_query(pending_users_query)

        query_list = list(cursor)

        if len(query_list) < 1:
            print('No pending approvals')
            return []

        cursor.close()

        return query_list

    def create_approval_req(self, user_aadhar, account_type):
        create_approval_request_query = self.root[15].text.format(user_aadhar, account_type)

        cursor = self.util.execute_query_with_commit(create_approval_request_query)

        cursor.close()

    def check_user_approved(self, aadhar):
        user_data = self.get_user(aadhar)
        if user_data[5] == 1:
            return True
    
        return False

    def delete_user(self, aadhar):
        delete_user_query = self.root[27].text.format(aadhar)

        cursor = self.util.execute_query_with_commit(delete_user_query)
        cursor.close()

    def get_all_admins(self):
        get_all_admins_query = self.root[29].text

        cursor = self.util.execute_stored_procedure(get_all_admins_query)

        if cursor == None:
            return []

        admins_list = []
        for data in cursor.stored_results():
            admins_list = data.fetchall()

        
        cursor.close()
        return admins_list