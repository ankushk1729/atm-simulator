from modules.account.controller import AccountController
from modules.auth.controller import AuthController
from modules.user.controller import UserController
from utils.util import Util

auth = AuthController()
auth.handler()

# user_controller = UserController()

# user_controller.create_user()

# user_controller.search_users_by_name()

# user_controller.get_user_data(123)

# print(authorize_permissions('8894e75d-247c-11ed-86be-544810d578e2', 'admin'))
