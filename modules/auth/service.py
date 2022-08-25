

#19:02

import hashlib
import uuid

from modules.user.service import UserService
from utils.connect import connection_obj


class AuthService:

    def __init__(self):
        self.cnx = connection_obj.getInstance()

    def encrypt_password(self, password):
        hash_string = password
        hash_string = hash_string.encode()
        return hashlib.sha256(hash_string).hexdigest()

    def signup(self, schema):
        
        hashedPassword = self.encrypt_password(schema['password'])

        unique_user_id = str(uuid.uuid1())

        query = "insert into users(id, full_name, email, password, phone, aadhar, DOB) values((%s), (%s), (%s), (%s), (%s), (%s), (%s))"

        cursor = self.cnx.cursor()

        cursor.execute(query, [unique_user_id, schema['full_name'], schema['email'], hashedPassword, schema['phone'], schema['aadhar'], schema['DOB']])

        self.cnx.commit()
        
        get_role_id_query = "select id from role where role_name = 'user'"

        cursor.execute(get_role_id_query)

        role_id = list(cursor)[0][0]

        create_user_role_mapping_query = "insert into user_role(role_id, user_id) values('{}', '{}')".format(role_id, unique_user_id)

        cursor.execute(create_user_role_mapping_query)

        self.cnx.commit()
        cursor.close()








    def login(self, email, password):
        
        search_user = "select * from users where email = '{}'".format(email)

        cursor = self.cnx.cursor()


        cursor.execute(search_user)

        queryList = list(cursor)

        if len(queryList) < 1 : 
            return False
            

        return cursor[0]

