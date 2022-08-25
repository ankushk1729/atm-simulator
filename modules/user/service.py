import xml.etree.ElementTree as ET

from utils.connect import connection_obj

tree = ET.parse('./config/queries.xml')

root = tree.getroot()
class UserService:

    def __init__(self):
        self.cnx = connection_obj.getInstance()

    def check_user_exists(self, param_key, param_value):
        query = "select aadhar, id from users where {} = (%s)".format(param_key)
        cursor = self.cnx.cursor()

        param_list = []
        param_list.insert(0, param_value)


        cursor.execute(query, param_list)
        queryList = list(cursor)
        cursor.close()

        if len(queryList) < 1: return False
        return True

    def approve_user(self, unique_field_key, unique_field_value):
        cursor = self.cnx.cursor()
        if unique_field_key == 'id':
            approve_user_query = root[4].text.format(unique_field_key, unique_field_value)
            cursor.execute(approve_user_query)
            self.cnx.commit()
            cursor.close()

        elif unique_field_key == 'aadhar':
            approve_user_query = root[5].text.format(unique_field_key, unique_field_value)
            cursor.execute(approve_user_query)
            self.cnx.commit()
            cursor.close()


    def search_users(self, search_key, search_value):

        search_user_query = root[6].text.format(search_value)
        
        cursor = self.cnx.cursor()

        try:
            cursor.execute(search_user_query)
        except:
            print('Unable to find the users')
            return []

        user_search_list = list(cursor)

        return user_search_list

    def get_user(self, aadhar):

        get_user_query = root[7].text.format(aadhar)

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
