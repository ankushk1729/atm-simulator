from config.db import *
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
        self.db.bind(provider = DB_PROVIDER,filename = DB_FILENAME, create_db = True) 

