#coding=utf-8
import urllib3
import os
import re
import logging

http = urllib3.PoolManager()
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
		
def getDataStr(url):
	r = get(url)
	if r:
		return str(r.data)
def getData(url):
	r = get(url)
	if r:
		return r.data
		
def getImg(html):
	#判空
	if not html:
		return
	else:
		reg = r'<img.*?src\s*=\s*[\"|\'](.+?)[\"|\'].*?>'
		imgre = re.compile(reg)
		imglist = re.findall(imgre,html)
		return imglist
		
#处理文图片件名
def handleImgName(url):
	fileName = url.split('?')[0].split('/')[-1];
	#如果文件没有后缀，默认不处理
	if fileName.find('.') == -1:
		return 
	else:
		return fileName
		
def my_urlencode(str) :
       reprStr = repr(str).replace(r'\x', '%')
       return reprStr[1:-1]
	   
def store(url):
	print('start...:' + url)
	fileName = handleImgName(url);
	if not fileName:
		return
	print("dowloading...:" + fileName)
	with open('F:\\work\\spider\\' + fileName,'wb') as f:
		img = getData(url)
		if img:
			f.write(img)
html = getDataStr("http://zhidao.baidu.com/link?url=ktZv96emvieLcNPWnrgdoteSifB16M1uUh9pWAb3zMjcR1l9AbanxnFAOUdU-zVH9hkdsj8PH_rpAmCApHcMv_")
imglist = getImg(html)

if imglist:
	for img in imglist:
		store(img)
