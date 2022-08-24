import mysql.connector
from config.db import *


class Connect:
   __instance = None
   @staticmethod 
   def getInstance():
      if Connect.__instance == None:
         Connect()
      return Connect.__instance.cnx

   def __init__(self):
      if Connect.__instance != None:
        raise Exception("Already instantialzed the connection")
      else:
        Connect.__instance = self
        self.cnx = mysql.connector.connect(user= DB_USER, password=DB_PASSWORD,host=DB_HOST,
                              database=DB_NAME)



connection_obj = Connect()
