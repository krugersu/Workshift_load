
import logging
import requests

import json
import os
import pathlib
from pathlib import Path
import tortilla
from pprint import pprint

class req1C:
     def __init__(self, nConfig):
          self.mConfig = nConfig
          
     def __enter__(self):
          return self

     def __exit__(self):
          self.close()
          
     def exeQuery(self,c_shop):
          try:
               r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.lquery)
# ?  r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test')
               r.encoding = 'utf-8' 
               c_count = r.json()
               return c_count
          except Exception as e:
               logging.exception(e, exc_info=False)
          return None
     
     
     
     
     def getQueryShop(self):
          
          try:
               r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.shopquery)
                    
            #   print(r.url)     
               r.encoding = 'utf-8' 
            #   print(r.status_code)
               c_count = r.json()
               listShop = self._getDirM(c_count)
               return listShop  # c_count
          except Exception as e:
               logging.exception(e, exc_info=False)
          return None     

     def shopForNumber(self,c_shop):
          
          mPar = {"number":str(c_shop)}
          print(mPar) 
          try:
               # r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
               #                     + self.mConfig._sections.one_C.port 
               #                     + self.mConfig._sections.one_C.lquery, params=mPar)
               
               n_shop = tortilla.wrap('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.lquery)
               c_count = n_shop.test_s.get('V1/test_1?number=' +str(c_shop))
               
               

# ?  r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test_1')
               # r.encoding = 'utf-8' 
              # c_count = r.json()
               return c_count
          except Exception as e:
               logging.exception(e, exc_info=False)
          return None

     def post_workshift(self,l_workshift):
         requests.post("http://bugs.python.org", data={'number': '12524', 'type': 'issue', 'action': 'show'})

     def _getDirM(self,listPath):
          
          listShop = []
          
          for curPath in listPath:
               curPath.replace('\\\\', '//')
               curPath = pathlib.PureWindowsPath(curPath)
               listShop.append(Path(curPath).parts[-1])
               listShop = list(set(listShop))
          return listShop
          






# github = tortilla.wrap('http://192.168.252.250:8082/UNF_test/hs/')
# user = github.test_s.get('V1/test_1?number=test')
# for item in user.barcodes:
    
#     print('---------')
#     pprint(item)
    
    
    
    
# def getQueryShop(self):
          
#           try:
#                r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
#                                    + self.mConfig._sections.one_C.port 
#                                    + self.mConfig._sections.one_C.shopquery)

#                print(r.url)     
#                r.encoding = 'utf-8' 
#                print(r.status_code)
#                c_count = r.json()
#                listShop = self._getDirM(c_count)
#             #   print(listShop)
#                return listShop  # c_count
#           except Exception as e:
#                logging.exception(e, exc_info=False)
#           return None         



