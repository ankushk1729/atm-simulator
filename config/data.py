from modules.account.controller import AccountController as AC
from modules.transaction.controller import TransactionController as TC
from modules.user.controller import UserController as UC

user_operations = ["view_details", "view_balance", "view_transactions", "withdraw", "deposit"]
admin_operations = ["search_users", "approve_user", "create_account", "create_user", "delete_user","view_all_users", "view_all_transactions", "search_users"]

admin_tasks_to_function_mapping = {
    "search_users": "Search users",
    "approve_user": "Approve a user",
    "create_account": "Create new account",
    "create_user": "Create a new user",
    "delete_user": "Delete a user",
    "view_all_users": "View all users",
    "view_all_transactions": "View all transactions",
    "get_user_transactions":"Get user transactions"
}

user_tasks_to_function_mapping = {
    "view_details": "View profile details",
    "view_balance": "View account balance",
    "view_transactions": "View transactions",
    "withdraw": "Withdraw money",
    "deposit": "Deposit money",
}
