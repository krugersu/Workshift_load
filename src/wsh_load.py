#!/usr/bin/python3.10

import os
import sys
import configparser
import m_config
import m_request


import app_logger
import db
import pathlib
from pathlib import Path

#: Global Constants
logger = app_logger.get_logger(__name__)
sys.path.insert(1, '/home/administrator/Workshift_load/src/')
"""Для логирования событий"""


# Functions
def main():
    """ Main program entry. """
    path = Path("config", "config.ini")
    logger.info("Start programs")

    tData = db.workDb(rc)
    rec_con = m_request.req1C(rc)

    # Список открытых смен от последнего зафиксированного времени
    l_workshift_open = tData.get_last_workshift_open()
    # Если нечего отправлять, то и отправляем
    if len(l_workshift_open) > 0:

        status_code = rec_con.post_workshift_open(l_workshift_open)
        # Меняем дату в файле только в случае успешного результата работы 1С
        if status_code == 200:
            tData.save_new_date_open()
        else:
            logger.info(u'status_code_open - ' + str(status_code))

    # Список закрытых смен от последнего зафиксированного времени
    l_workshift = tData.get_last_workshift()
    # Если нечего отправлять, то и отправляем
    if len(l_workshift) > 0:
        # rec_con = m_request.req1C(rc)
        status_code = rec_con.post_workshift(l_workshift)
        # Меняем дату в файле только в случае успешного результата работы 1С
        if status_code == 200:
            tData.save_new_date()
        else:
            logger.info(u'status_code - ' + str(status_code))

    logger.info(u'End programs')


if __name__ == "__main__":

    m_conf = m_config.m_Config()
    rc = m_conf.loadConfig()
    if not rc == None:
        main()
    else:
        logger.info(u'Программа завершила работу')
