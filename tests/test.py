from modules.account.service import AccountService
from modules.auth.service import AuthService
from modules.user.service import UserService


def test_login_output():
    auth_service = AuthService()

    user_info = auth_service.login('admin@root.com', 'pass')

    assert user_info[7] == 'admin@root.com'


def test_get_user():
    user_service = UserService()
    aadhar = 69
    user_info = user_service.get_user(aadhar)

    assert len(user_info) == 11

    assert user_info[1] == 'nice'


def get_account_name(account_id):
    account_service = AccountService()
    return account_service.get_account_name_by_id(account_id)


def test_get_account_name_from_id(mocker):
    func = mocker.patch('modules.account.service.AccountService.get_account_name_by_id', return_value = 'savings')

    result = func(1)

    assert get_account_name(1) == 'savings'
