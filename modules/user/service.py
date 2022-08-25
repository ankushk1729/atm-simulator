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
            cursor = self.util.execute_query_with_commit()
            cursor.close()

        elif unique_field_key == 'aadhar':
            approve_user_query = self.root[5].text.format(unique_field_key, unique_field_value)
            cursor.execute(approve_user_query)
            self.cnx.commit()
            cursor.close()


    def search_users(self, search_key, search_value):

        search_user_query = self.root[6].text.format(search_value)
        
        cursor = self.cnx.cursor()

        try:
            cursor.execute(search_user_query)
        except:
            print('Unable to find the users')
            return []

        user_search_list = list(cursor)

        return user_search_list

    def get_user(self, aadhar):

        get_user_query = self.root[7].text.format(aadhar)

        cursor = self.cnx.cursor()

        try:
            cursor.execute(get_user_query)
        except:
            print('Unable to find the user')
            return None

        users_list = list(cursor)
        if len(users_list) < 1 : 
            return None

        user = users_list[0]
        return user

    def get_all_users(self):
        get_users_query = self.root[10].text


        cursor = self.util.execute_query(get_users_query)

        if len(list(cursor)) < 1 : 
            return []

        return list(cursor)
