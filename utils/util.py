import xml.etree.ElementTree as ET

from utils.connect import connection_obj

tree = ET.parse('./config/queries.xml')


class Util:

    def __init__(self):
        self.root = tree.getroot()
        self.cnx = connection_obj.getInstance()


    def get_query_root(self):
        return self.root

    def execute_query(self, query):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(query)
            return cursor
        except:
            print('Unable to perform the action')
            return None

    def execute_query_with_commit(self, query):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(query)
            self.cnx.commit()
            return cursor
        except:
            print('Unable to perform the action')
            return None

    def execute_stored_procedure(self, sp):
        try:
            print(sp)
            cursor = self.cnx.cursor()
            cursor.callproc('sp_getAdmins', [])
            cursor.stored_results()
            return cursor
        except:
            print('Unable to perform the action')
            return None

    def authorize_permissions(self, user_id, role):
        try:
            root = self.get_query_root()
            search_role_id_query = root[8].text.format(user_id)

            cursor = self.execute_query(search_role_id_query)
            search_list = list(cursor)
            role_id = search_list[0][0]

            search_role_name_query = root[9].text.format(role_id)
            cursor = self.execute_query(search_role_name_query)

            search_list = list(cursor)
            role_name = search_list[0][0]
            cursor.close()
        except:
            print('Unable to perfrom the action')
            return False
        if role_name == role:
            return True
        return False
