import xml.etree.ElementTree as ET

import mysql.connector

tree = ET.parse('./config/settings.xml')

root = tree.getroot()


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
        #print(root[0].text, root[1].text, root[2].text, root[3].text)
        self.cnx = mysql.connector.connect(user= "bhawana", password="mysqlpassword",host="localhost",
                              database="atm")



connection_obj = Connect()
