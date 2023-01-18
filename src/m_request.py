
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


     def post_workshift(self, l_workshift):

          try:
               r = requests.post('http://' + self.mConfig._sections.one_C.server_ip + ':'
                                   + self.mConfig._sections.one_C.port
                                   + self.mConfig._sections.one_C.workshift, data=None, json= l_workshift)

          except Exception as e:
               logging.info(u'status_code - ' + str(r.status_code))
               logging.exception(e, exc_info=False)

          return (r.status_code)

     def post_workshift_open(self, l_workshift_open):

          try:
               r = requests.post('http://' + self.mConfig._sections.one_C.server_ip + ':'
                                   + self.mConfig._sections.one_C.port
                                   + self.mConfig._sections.one_C.workshift_open, data=None, json= l_workshift_open)

          except Exception as e:
               logging.info(u'status_code - ' + str(r.status_code))
               logging.exception(e, exc_info=False)

          return (r.status_code)
