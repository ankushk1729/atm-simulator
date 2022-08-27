
from modules.account.service import AccountService
from modules.transaction.service import TransactionService
from prettytable import PrettyTable


class TransactionController:
    
    def __init__(self, user_info):
        self.user_info = user_info
        self.transaction_service = TransactionService()
        self.account_service = AccountService(user_info)


    def get_all_txns(self):
        txns_list = self.transaction_service.get_all_txns()
        txn_table = PrettyTable()
        txn_table.field_names = ['Transaction id', 'Amount', 'Account num', 'Transaction Type']
        for txn in txns_list:
            txn_table.add_row((txn[0], txn[2], txn[3], txn[5]))

        print('\nHere are the transactions')
        print(txn_table)

    def get_user_txns(self):
        user_accounts = self.account_service.get_user_accounts(self.user_info[3])


        user_account_list = [x[0] for x in user_accounts]

        user_account_nums = tuple(user_account_list)

        user_txns_ = []
        for user_account in user_account_nums:
            user_txns_.insert(len(user_txns_), self.get_account_txns(user_account))

        user_txns = [item for sublist in user_txns_ for item in sublist]
        print(user_txns)
        user_txns_table = PrettyTable()
        user_txns_table.field_names = ['Transaction id', 'Account number', 'amount', 'Transaction type']
        for txn in user_txns:
            if len(txn) == 0 : continue
            user_txns_table.add_row((txn[0], txn[3], txn[2], txn[5]))

        print('\nHere are your transactions')
        print(user_txns_table)
        
    def get_account_txns(self, account_num):
        account_txns = self.transaction_service.get_account_transactions(account_num)
        return account_txns

    def account_selection(self):
        user_accounts = self.account_service.get_user_accounts(self.user_info[3])
        print(user_accounts)
        user_account_list = [x[0] for x in user_accounts]
        user_accounts_table = PrettyTable()
        user_accounts_table.field_names = ['Account number', 'balance', 'name']
        for account in user_accounts:
            user_accounts_table.add_row((account[0], account[1], account[7]))

        while True:
  
            print('\nHere are your accounts')
            print(user_accounts_table)
            try:
                choice = input('Select the account number : ')
                print('Or enter 0 to exit')
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if int(choice) == 0:
                    return 0
                if not int(choice) in user_account_list : raise ValueError('Please enter a valid account number from the above options')
                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))
        
        return int(choice)


    def withdraw(self):

        account_num = self.account_selection()
        account_info = self.account_service.get_account_info(account_num)
        max_withdrawal_amount = account_info[7]
        min_balance = account_info[8]
        account_balance = account_info[1]
        account_type_name = account_info[9]
        
        if account_balance <= 0:
            print('Sorry no balance to withdraw money')
            return
        while True:
            try:
                withdrawal_amount_choice = input('Enter the amount you want to withdraw : ')
                if not withdrawal_amount_choice.isdigit() : raise TypeError('Invalid input, please enter a number')
            except TypeError as error:
                print(str(error))

            withdrawal_amount = int(withdrawal_amount_choice)
            if account_type_name == 'savings':
                if withdrawal_amount > max_withdrawal_amount:
                    print('Sorry max withdrawal amount for {} account is {}'.format(account_type_name, max_withdrawal_amount))
                elif account_balance < withdrawal_amount :
                    print("Sorry you don't have that much balance in your account, your balance is {}".format(account_balance))
                elif (account_balance - min_balance ) < withdrawal_amount:
                    print('Sorry you have to maintain a minimum balance of {} for your {} account'.format(min_balance, account_type_name))
                else :
                    break
            elif account_type_name == 'current' :
                if account_balance < withdrawal_amount :
                    print("Sorry you don't have that much balance in your account, your balance is {}".format(account_balance))
                elif (account_balance - min_balance ) < withdrawal_amount:
                    print('Sorry you have to maintain a minimum balance of {} for your {} account'.format(min_balance, account_type_name))
                else :
                    break

        updated_balance = account_balance - withdrawal_amount
        try:
            self.transaction_service.create_txn(updated_balance, account_num, 'withdrawal')
            self.account_service.update_balance(withdrawal_amount, account_num)
        except:
            pass

        print('Withdrawal is successful')
    def deposit():
        pass
