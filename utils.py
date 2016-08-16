#coding=utf-8
from analysis import Page
import os
from log import logging

#����list
def getImgUrl(html):
	#�п�
	if not html:
		return
	else:
		page = Page(html)
		attrs = page.getElementAttrs('img')
		
		imglist = []
		for attr in attrs:
			imglist.append(attr.get('src'))
		
		return imglist

#�Ѵ��ڱ�֤�����쳣
#��֧�ֶ༶����	
#path֧��list��tuple���ַ���
#�ָ���������ϵ�ǰ����ϵͳ	
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
	