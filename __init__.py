#coding=utf-8
import utils
import os

#生成的主目录
tmp = 'tmp'
#抓取文件的下载目录
spiderPath = tmp + os.path.sep + 'spider' + os.path.sep
catelogPath = tmp + os.path.sep + "catalog.txt"
#日志文件
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