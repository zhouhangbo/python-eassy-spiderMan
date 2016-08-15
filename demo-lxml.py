#coding=utf-8
import uuid
import urllib3
import os
import re
from log import logging
import utils
from __init__ import *

http = urllib3.PoolManager()
file_path = Constants.spiderPath
catelogPath = Constants.catelogPath
#��ʼ���ļ���
utils.mkdir(file_path)

url = "http://zhidao.baidu.com/link?url=ktZv96emvieLcNPWnrgdoteSifB16M1uUh9pWAb3zMjcR1l9AbanxnFAOUdU-zVH9hkdsj8PH_rpAmCApHcMv_"

#get���� ����response
def get(url):
	try:
		r = http.request('GET',url)
		if r.status == 200:
			return r
		else:
			return
	except BaseException as e:
		return
		#logging.error('ResponseError:',e)
		
def getDataStr(url):
	r = get(url)
	if r:
		return str(r.data)
def getData(url):
	r = get(url)
	if r:
		return r.data
				
#������ͼƬ����
def handleImgName(url):
	fileName = url.split('?')[0].split('/')[-1];
	#����ļ�û�к�׺���Զ������ļ���
	if fileName.find('.') == -1:
		return str(uuid.uuid1()) + '.jpg'
	else:
		return fileName
		
def my_urlencode(str) :
       reprStr = repr(str).replace(r'\x', '%')
       return reprStr[1:-1]
	   
#ʹ������
def getImg(html):
	#�п�
	if not html:
		return
	else:
		reg = r'<img.*?src\s*=\s*[\"|\'](.+?)[\"|\'].*?>'
		imgre = re.compile(reg)
		imglist = re.findall(imgre,html)
		return imglist

		
def store(url):
	fileName = handleImgName(url);
	global newName
	if not fileName:		
		return
	
	with open(file_path + fileName,'wb') as f:
		img = getData(url)
		if img:
			logging.info("dowloading...:" + fileName)
			print("dowloading...:" + fileName)
			newName = fileName
			f.write(img)
html = getDataStr(url)
imglist = utils.getImgUrl(html)

if imglist:
	list = []
	catalog = ''
	for url in imglist:
		store(url)
		catalog += url + '  ' + newName + '\n'
	with open(catelogPath,'a') as f:
		f.write(catalog)
