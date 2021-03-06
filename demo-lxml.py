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
#初始化文件夹
utils.mkdir(file_path)

url = "http://limu.iteye.com/blog/1013223"

#get请求 返回response
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
				
#处理文图片件名
def handleImgName(url):
	fileName = url.split('?')[0].split('/')[-1];
	#如果文件没有后缀，自动生成文件名
	if fileName.find('.') == -1:
		return str(uuid.uuid1()) + '.jpg'
	else:
		return fileName
		
def my_urlencode(str) :
       reprStr = repr(str).replace(r'\x', '%')
       return reprStr[1:-1]
	   
#使用正则
def getImg(html):
	#判空
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
