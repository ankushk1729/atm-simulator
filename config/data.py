from modules.account.controller import AccountController as AC
from modules.transaction.controller import TransactionController as TC
from modules.user.controller import UserController as UC

user_operations = ["view_details", "view_balance", "view_transactions", "withdraw", "deposit"]
admin_operations = ["search_user", "approve_user", "create_account", "create_user", "delete_user","view_all_users", "view_all_transactions"]

# admin_tasks_to_function_mapping = {
#     "search_user": ("Search a user", UC.search_users_by_name),
#     "approve_user": ("Approve a user", UC.approve_user_by_unique_key),
#     "create_account": ("Create new account", AC.create_account),
#     "create_user": ("Create a new user", UC.create_user),
#     "delete_user": ("Delete a user", UC.delete_user),
#     "view_all_users": ("View all users", UC.get_all_users),
#     "view_all_transactions": ("View all transactions", TC.get_all_txns)
# }

# user_tasks_to_function_mapping = {
#     "view_details": ("View profile details", UC.get_current_user_data),
#     "view_balance": ("View account balance", AC.get_balance),
#     "view_transactions": ("View transactions", TC.get_user_txns),
#     "withdraw": ("Withdraw money", TC.withdraw),
#     "deposit": ("Deposit money", TC.deposit),
# }
