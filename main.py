from modules.auth.controller import AuthController
from modules.user.controller import UserController

# auth = AuthController()
# auth.handler()


user_controller = UserController()

user_controller.create_user()
