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
        
        self.cnx = mysql.connector.connect(user= root[0].text, password=root[1].text,host=root[2].text,
                              database=root[3].text)



connection_obj = Connect()
