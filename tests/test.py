# from unittest.mock import Mock



from modules.account.service import AccountService
from modules.auth.service import AuthService
from modules.user.service import UserService


def test_login_output():
    auth_service = AuthService()

    user_info = auth_service.login('admin@root.com', 'pass')

    assert user_info[7] == 'admin@root.com'


def test_get_user():
    user_service = UserService()
    aadhar = 45
    user_info = user_service.get_user(aadhar)

    assert len(user_info) == 11

    assert user_info[1] == 'dino'


def test_get_account_name_from_id():

    account_service = AccountService()
    account_name = account_service.get_account_name_by_id(1)

    assert account_name == 'savings'


def test_age():
    my_date = '17/04/2001'

    b_date = datetime.strptime(my_date, '%d/%m/%Y')

    age = round(((datetime.today() - b_date).days/365))

    assert age == 21
