import hashlib

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

        query = "insert into users(full_name, email, password, phone, aadhar, DOB) values((%s), (%s), (%s), (%s), (%s), (%s))"

        cursor = self.cnx.cursor()

        cursor.execute(query, [schema['full_name'], schema['email'], hashedPassword, schema['phone'], schema['aadhar'], schema['DOB']])

        self.cnx.commit()

        cursor.close()

    # Pending sql injection check
    def login(self, email, password):
        
        user_service = UserService()
        if not user_service.check_user_exists('email', email): 
            print("User doesn't exist")
            return 0
        else : return 1

