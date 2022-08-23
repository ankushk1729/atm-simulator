from pony import orm


class Connect:
   __instance = None
   @staticmethod 
   def getInstance():
      if Connect.__instance == None:
         Connect()
      return Connect.__instance.db

   def __init__(self):
      if Connect.__instance != None:
        raise Exception("Already instantialzed the connection")
      else:
        Connect.__instance = self
        self.db = orm.Database()
        self.db.bind(provider='sqlite',filename="pony_test.db", create_db = True) 

