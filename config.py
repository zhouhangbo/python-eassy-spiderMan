#coding=utf-8
import utils
import os

#���ɵ���Ŀ¼
tmp = 'tmp'
#ץȡ�ļ�������Ŀ¼
spiderPath = tmp + os.path.sep + 'spider' + os.path.sep
catelogPath = tmp + os.path.sep + "catalog.txt"
#��־�ļ�
logPath = tmp + os.path.sep + 'logger.log'

class Constants():
	tmp = tmp
	spiderPath = spiderPath
	catelogPath = catelogPath
	logPath = logPath
Constants = Constants()
__all__ = [
	'Constants'
]