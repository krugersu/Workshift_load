#/usr/bin/env python3.11
# Imports
import os
import sys
import configparser
import m_config



import app_logger
import db
import pathlib
from pathlib import Path 

#: Global Constants
logger = app_logger.get_logger(__name__)
"""Для логирования событий"""



# Functions
def main():
    """ Main program entry. """

    path = Path("config", "config.ini") 
    logger.info("Start programs")

    # Анализ в каких магазинах изменения
    tData = db.workDb(rc)
    tData.get_last_workshift()
    logger.info(u'End programs')   



if __name__ == "__main__":

    m_conf = m_config.m_Config()   
    rc =  m_conf.loadConfig()
    if not rc == None:
        main()
    else:
        logger.info(u'Программа завершила работу')                                      


