from modules.auth.controller import AuthController
from modules.user.controller import UserController

# auth = AuthController()
# auth.handler()


user_controller = UserController()

# user_controller.create_user()

# user_controller.search_users_by_name()

user_controller.get_user_data(123)
