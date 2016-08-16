#coding=utf-8
from analysis import Page
import os
from log import logging

#返回list
def getImgUrl(html):
	#判空
	if not html:
		return
	else:
		page = Page(html)
		attrs = page.getElementAttrs('img')
		
		imglist = []
		for attr in attrs:
			imglist.append(attr.get('src'))
		
		return imglist

#已存在保证不跑异常
#可支持多级创建	
#path支持list、tuple或字符串
#分隔符必须符合当前操作系统	
def mkdir(path):
	dirs = None
	if isinstance(path,list) or isinstance(path,tuple):
		dirs = path
	else:
		dirs = path.split(os.sep)
	directory = ''
	for folder in dirs:
		directory = os.path.join(directory,folder)
		try:		
			os.mkdir(directory)
		except BaseException as e:
			logging.error(e)
			
if __name__ == '__main__':
	mkdir(os.path.join('tmp1','ww','ss'))
	