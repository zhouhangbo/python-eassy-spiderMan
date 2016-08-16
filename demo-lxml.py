#coding=utf-8
import uuid
from my_http import http
import os
import re
from log import logging
import utils
import chardet
from config import *

file_path = Constants.spiderPath
catelogPath = Constants.catelogPath
#��ʼ���ļ���
utils.mkdir(file_path)

url = "http://limu.iteye.com/blog/1013223"

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
		
def getData(url):
	r = get(url)
	if r:
		print(type(r.data))
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
	img = getData(url)
	if img:
		with open(file_path + fileName,'wb') as f:
			logging.info("dowloading...:" + fileName)
			print("dowloading...:" + fileName)
			newName = fileName
			f.write(img)
	else:
		logging.error('dowload error with:' + url)
		
html = getData(url)
imglist = utils.getImgUrl(html)

if imglist:
	list = []
	catalog = ''
	for url in imglist:
		store(url)
		catalog += url + '  ' + newName + '\n'
	with open(catelogPath,'a') as f:
		f.write(catalog)
