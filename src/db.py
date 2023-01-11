
import json
from types import SimpleNamespace
from pathlib import Path  
import diff_data
import logging
from datetime import datetime
from pprint import pprint


import pymysql




class workDb:
    def __init__(self,rc, c_count = None):
        
        
        self.mydb = pymysql.connect(host=rc._sections.artix.server_ip,
            database=rc._sections.artix.database,
            user=rc._sections.artix.user,
            passwd=rc._sections.artix.passwd)
        self._mycursor = self.mydb.cursor() #cursor created

    
    
        
    def get_last_workshift(self):
        
        l_date = self.load_last_date()
        self._mycursor.execute(diff_data.qrSelect_workshift, [l_date])
        l_workshift = self._mycursor.fetchall()
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(l_workshift, f, ensure_ascii=False, indent=4)
        #self.mydb.close()
        
        logging.info('sent workshift for 1C')
        logging.info('workshift - ' + str(l_workshift))
        
        tl_date = self.get_last_date()
        self.save_last_date(tl_date)
        
        return l_workshift


    def save_last_date(self,t_date):
        filename = 'last_date.txt'
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write(str(t_date))
            

    
    
    def load_last_date(self):
        filename = 'last_date.txt'
        with open(filename, 'r', encoding='utf-8') as outfile:
            return (outfile.readline())
            

        
    def get_last_date(self):
        
        self._mycursor.execute(diff_data.qrSelect_last_workshift_date)
        l_date = self._mycursor.fetchone()
        
        self.mydb.close()
        
        return l_date[0]
        
        


