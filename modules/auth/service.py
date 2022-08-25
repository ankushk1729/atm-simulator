

import xml.etree.ElementTree as ET

tree = ET.parse('./config/queries.xml')

root = tree.getroot()

import hashlib
import uuid

from utils.connect import connection_obj


class AuthService:

    def __init__(self):
        self.cnx = connection_obj.getInstance()

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

        create_user_query = root[0].text.format(unique_user_id, schema['full_name'], schema['email'], hashedPassword, schema['phone'], schema['aadhar'], schema['DOB'])

        cursor = self.cnx.cursor()

        # Improve
        try:
            cursor.execute(create_user_query)
            self.cnx.commit()
        except:
            return False


        cursor.execute(root[1].text)

        role_id = list(cursor)[0][0]

        create_user_role_mapping_query = root[2].text.format(role_id, unique_user_id)

        cursor.execute(create_user_role_mapping_query)

        self.cnx.commit()
        cursor.close()

        return unique_user_id


    def login(self, email, password):
        
        search_user = root[3].text.format(email)

        cursor = self.cnx.cursor()

        print(search_user)

        cursor.execute(search_user)

        queryList = list(cursor)

        if len(queryList) < 1 : 
            return False

        user_password = queryList[0][2]       
        is_password_correct = self.compare_password(password, user_password)

        if not is_password_correct :
            return False

        cursor.close()
        return queryList[0]

