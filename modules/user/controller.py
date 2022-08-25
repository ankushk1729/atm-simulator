
from modules.auth.controller import AuthController
from modules.user.service import UserService


class UserController:

    def __init__(self):
        self.user_service = UserService()
    
    def create_user(self):
        auth_controller = AuthController()

        (user_id, aadhar) = auth_controller.signup()
        print(user_id)
        self.approve_user_by_unique_key('id', str(user_id))

    def approve_user_by_unique_key(self, unique_field_key, unique_field_value):

        self.user_service.approve_user(unique_field_key, unique_field_value)

    def get_all_users(self):
        pass

    def get_user(self):
        pass
