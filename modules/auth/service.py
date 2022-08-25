

import hashlib
import uuid

from utils.util import Util


class AuthService:

    def __init__(self):
        self.util = Util()
        self.root = self.util.get_query_root()

    def encrypt_password(self, password):
        hash_string = password
        hash_string = hash_string.encode()
        return hashlib.sha256(hash_string).hexdigest()

    def compare_password(self, candidate_password, password):
        hash_string = candidate_password
        hash_string = hash_string.encode()
        return hashlib.sha256(hash_string).hexdigest() == password

    def signup(self, schema):
        
        hashedPassword = self.encrypt_password(schema['password'])

        unique_user_id = str(uuid.uuid1())

        create_user_query = self.root[0].text.format(unique_user_id, schema['full_name'], schema['email'], hashedPassword, schema['phone'], schema['aadhar'], schema['DOB'])

        try:
            cursor = self.util.execute_query_with_commit(create_user_query)
        except:
            return False


        cursor = self.util.execute_query(self.root[1].text)

        role_id = list(cursor)[0][0]

        create_user_role_mapping_query = self.root[2].text.format(role_id, unique_user_id)

        cursor = self.util.execute_query_with_commit(create_user_role_mapping_query)

        cursor.close()

        return unique_user_id


    def login(self, email, password):
        
        search_user = self.root[3].text.format(email)

        cursor = self.util.execute_query(search_user)

        queryList = list(cursor)

        if len(queryList) < 1 : 
            return False

        user_password = queryList[0][2]       
        is_password_correct = self.compare_password(password, user_password)

        if not is_password_correct :
            return False

        cursor.close()
        return queryList[0]

