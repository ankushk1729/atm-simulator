from utils.connect import connection_obj


class UserService:

    def __init__(self):
        self.cnx = connection_obj.getInstance()

    def check_user_exists(self, aadhar):
        query = "select aadhar, id from users where aadhar = (%s)"
        cursor = self.cnx.cursor()

        aadhar_value = []
        aadhar_value.insert(0, aadhar)


        cursor.execute(query, aadhar_value)

        queryList = list(cursor)
    
        cursor.close()

        if len(queryList) < 1: return False
        return True

