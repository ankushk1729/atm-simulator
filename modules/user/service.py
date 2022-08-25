from utils.connect import connection_obj


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

