from utils.util import Util


class TransactionService:
    def __init__(self) :
        self.util = Util()
        self.root = self.util.get_query_root()
        
    def get_all_txns(self):
        get_txns_query = self.root[19].text

        cursor = self.util.execute_query(get_txns_query)

        if cursor == None:
            return
        
        txns_list = list(cursor)
        return txns_list





