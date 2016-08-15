#coding=utf-8
import logging
from __init__ import *
print(Constants.logPath)
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=Constants.logPath,
                filemode='a')
    
