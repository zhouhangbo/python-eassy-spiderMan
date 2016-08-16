#coding=utf-8
from lxml import etree

class Page(object):
	
	def __init__(self, html):
		self.html = html
		self.page = etree.HTML(html)
	#获得某个标签的属性
	#返回结果[{},{}]dict数组
	def getElementAttrs(self, ele):
		eles = self.page.xpath('//' + ele);
		attrs = []
		for e in eles:
			attr = e.attrib
			attrs.append(attr)
		return attrs

html = "<html><body><img src='123' style=\"32\"></body></html>"		
if __name__ == '__main__':
	page = Page(html)
	print(page.html)
	print(page.getElementAttrs('img'))