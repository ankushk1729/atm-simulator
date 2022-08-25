from service import TransactionService
from account.service import AccountService 
from exception import MyError
class TransactionController:
    # Examples functions
    def __init__(self, user_info_obj):  
        self.user_info= user_info_obj
        self.current_userid=self.user_info[0]
        self.transaction_service=TransactionService()
        self.account_service=AccountService()
        self.balance=TransactionService.get_balance(self.current_userid)
        acc_type=TransactionService.get_acctype()

    def deposit(self):
        amount=int(input("Enter amt to be deposited."))
        updated_balance=self.balance+amount
        self.transaction_service.create_transaction("deposit", amount, 1234 )
        self.account_service.update_balance(self.current_userid,updated_balance,int(self.choice))
        

    def withdrawal(self,amount):   #CONSIDERING 0-SAVINGS, 1-CURRENT
        [max_withdrawal_amount,min_balance]=self.account_service.get_acc_properties(self.current_userid)
        try:
            if amount<=max_withdrawal_amount:
                if self.balance-amount<min_balance:
                    raise MyError("Can't withdraw {}, min amt to be maintained is {}}".format(amount,min_balance))
                else:
                    updated_balance=self.balance-amount
                    TransactionService.update_balance(updated_balance)
            else:
                raise MyError("Can't withdraw more than {} from a saving's acc".format(max_withdrawal_amount))        
        except MyError as error:
            print(error.value)


    def get_all_txns(self):
        all_transac=TransactionService.get_alltransac()
        for i in all_transac:
            print(i)
        
