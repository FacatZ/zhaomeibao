from app.models import User, ProductInformation, Category, IndustryIndex, ArticleCategory, Article
from sqlalchemy import and_
from flask import request

class Pagination(object):
	def __init__(self, obj_query, page, per_page):
		self.items = obj_query.offset((page-1)*per_page).limit(per_page)
		self.query = obj_query
		self.total = obj_query.count()
		self.per_page = per_page
		self.page = page
		self.pages = int((self.total + self.per_page - 1)/self.per_page) 
		self.has_prev = False if self.page == 1 else False
		self.has_next = False if self.page == self.pages else False
		self.prev_num = self.page - 1
		self.next_num = self.pages - self.page
	def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
		last = 0
		for num in xrange(1, self.pages + 1):
			if num <= left_edge or \
				(num > self.page - left_current - 1 and \
				num < self.page + right_current) or \
				num > self.pages - right_edge:
				if last + 1 != num:
					yield None
				yield num
				last = num

		

def getProductInformationByArea(areaId, num=10):
	return ProductInformation.query.filter_by(areaid=areaId).limit(num)

def preprocessingArticleDict():
	return {
		'title': request.form.get('title', '', type=str),
		'body': request.form.get('body', '', type=str),
		'ctgid': request.form.get('ctgid', 1, type=int)
	}

def preprocessingProductInformationDict():
	return {
		'typeid': request.form.get('typeid', 0, type=int),
		'pdpid': request.form.get('pdpid', 1, type=int),
		'pdcid': request.form.get('pdcid', 1, type=int),
		'coal': request.form.get('coal', '', type=str),
		'count': request.form.get('count', 0, type=int),
		'price': request.form.get('price', 0, type=int),
		
		'prtype': request.form.get('prtype', '', type=str),
		'prpid': request.form.get('prpid', 1, type=int),
		'prcid': request.form.get('prcid', 1, type=int),
		
		'vldterm': request.form.get('vldterm', '', type=str),

		'dppid': request.form.get('prpid', 1, type=int),
		'dpcid': request.form.get('prcid', 1, type=int),
		'dpaddr': request.form.get('dpaddr', '', type=str),

		'paytype': request.form.get('paytype', '', type=str),
		'remark': request.form.get('remark', '', type=str)
	}

def preprocessingIndutrialIndex():
	return {
		'mt': request.form.get('mt', 0.0, type=float),
		'mad': request.form.get('mad', 0.0, type=float),
		'var': request.form.get('var', 0.0, type=float),
		'vad': request.form.get('vad', 0.0, type=float),
		'vdaf': request.form.get('vdaf', 0.0, type=float),
		'aar': request.form.get('aar', 0.0, type=float),
		'aad': request.form.get('aad', 0.0, type=float),
		'fcar': request.form.get('fcar', 0.0, type=float),
		'fcad': request.form.get('fcad', 0.0, type=float),
		'star': request.form.get('start', 0.0, type=float),
		'stad': request.form.get('stad', 0.0, type=float),
		'qnetar': request.form.get('qnetar', 0, type=int),
		'qnetad': request.form.get('qnetad', 0, type=int),
		'szuplm': request.form.get('szuplm', 0, type=int),
		'szlowlm': request.form.get('szlowlm', 0, type=int),
		'szppt': request.form.get('szppt', 0, type=int)
	}



def processingIndustrialIndex():
	ii_dict = preprocessingIndutrialIndex()
	return IndustryIndex.from_dict(ii_dict)

def processingProductInformation():
	pi_dict = preprocessingProductInformationDict()
	return ProductInformation.from_dict(pi_dict)

def processingCategory():
	cid = request.form.get('ctgid', 1, type=int)
	return Category.query.filter_by(id=cid).first()

# def processingModifyProductInformation(product):
# 	product_dict = preprocessingProductInformationDict()
# 	product.modify_from_dict()
# 	return True