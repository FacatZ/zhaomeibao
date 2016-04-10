#coding=utf-8
from app.models import User, ProductInformation, Category, IndustryIndex, ArticleCategory, Article, OrderNumberRecord
from sqlalchemy import and_, or_
from flask import request, url_for
from ..database import db_session
import bleach
import profile

class Pagination(object):
	def __init__(self, obj_query, page, per_page):
		self.items = obj_query.offset((page-1)*per_page).limit(per_page)
		self.query = obj_query
		self.total = obj_query.count()
		self.per_page = per_page
		self.page = page
		self.pages = int((self.total + self.per_page - 1)/self.per_page) 
		self.has_prev = False if self.page == 1 else True
		self.has_next = False if self.page == self.pages else True
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
	d = {
		'title': request.form.get('title', '', type=unicode),
		'body': request.form.get('body', '', type=unicode),
		'ctgid': request.form.get('ctgid', 1, type=int)
	}
	return d

def preprocessingProductInformationDict():
	d = { 
		'typeid': request.form.get('typeid', 0, type=int),
		'pdpid': request.form.get('pdpid', -2, type=int),
		'pdcid': request.form.get('pdcid', -2, type=int),
		'coal': request.form.get('coal', '', type=unicode),
		'count': request.form.get('count', 0, type=int),
		'price': request.form.get('price', 0, type=float),
		'stock': request.form.get('stock', 0, type=int),
		'prtype': request.form.get('prtype', '', type=unicode),
		'prpid': request.form.get('prpid', -2, type=int),
		'prcid': request.form.get('prcid', -2, type=int),
		
		'vldterm': request.form.get('vldterm', '', type=unicode),

		'dppid': request.form.get('dppid', -2, type=int),
		'dpcid': request.form.get('dpcid', -2, type=int),
		'dpaddr': request.form.get('dpaddr', '', type=unicode),

		'prtype': request.form.get('prtype', '', type=unicode),
		'pdtype': request.form.get('pdtype', 0, type=int),
		'paytype': request.form.get('paytype', '', type=unicode),
		'remark': request.form.get('remark', '', type=unicode)
	}
	return d

def preprocessingIndutrialIndex():
	d = {
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
	return d

def preprocessingProductInformationModifyDict():
	olddict = preprocessingProductInformationDict()
	newdict = {}
	newdict['ctgid'] = request.form.get('ctgid', 0, type=int)
	not_allowed_key = ['typeid']
	filter_area_key = ['pdpid', 'pdcid', 'dppid', 'dpcid', 'prpid', 'prcid']
	for k,v in olddict.iteritems():
		if (k in not_allowed_key) or (k in filter_area_key and v == -2):
			continue
		newdict[k] = v
	return newdict

def processingIndustrialIndex():
	ii_dict = preprocessingIndutrialIndex()
	return IndustryIndex.from_dict(ii_dict)

def processingProductInformation():
	pi_dict = preprocessingProductInformationDict()
	print 'ProductInformation dictionary:', pi_dict
	print 'full form:', request.form
	return ProductInformation.from_dict(pi_dict)

def processingCategory():
	cid = request.form.get('ctgid', 1, type=int)
	return Category.query.filter_by(id=cid).first()



def processingCategory():
	cid = request.form.get('ctgid', 1, type=int)
	return Category.query.filter_by(id=cid).first()

def getStockProducingArea():
	return profile.ChandiSettingDictionary

def getStockJiaogeArea():
	return profile.JiaogeGroupName

def getStockQnet():
	return profile.QnetSettingDictionary

def getStockSt():
	return profile.StSettingDictionary

def getStockV():
	return profile.VSettingDictionary

def getStockMt():
	return profile.MtSettingDictionary
# def processingModifyProductInformation(product):
# 	product_dict = preprocessingProductInformationDict()
# 	product.modify_from_dict()
# 	return True

# def processingModifyProductInformation(product):
# 	product_dict = preprocessingProductInformationDict()
# 	product.modify_from_dict()
# 	return True
def filterUserInput(value):
	allowed_tags = profile.allowed_tags
	return bleach.linkify(bleach.clean(value, tags=allowed_tags, strip=True))



def generate_unique_serial_number(pdtype=0):
	import datetime

	print '-----pdtype:',pdtype
	ordernum = 'GH' if pdtype == 1 else 'XQ'
	ghorder = OrderNumberRecord.query.filter_by(pdtype=pdtype).first()

	if not ghorder:
		return None

	last_date = ghorder.last_date
	count = ghorder.count

	today = datetime.date.today()
	if str(today) > str(last_date).split(' ')[0]:
		last_date = today
		ghorder.last_date = today
		count = 1
	else:
		count = count + 1
	ghorder.count = count
	db_session.add(ghorder)
	db_session.commit()

	ordernum = ordernum + ''.join(str(today).split(' ')[0].split('-')) + '{count:06}'.format(count=count)
	print ordernum
	return ordernum

def Qnet_filter(id):
	if id == 5001:
		return and_(IndustryIndex.qnetar >=1500, IndustryIndex.qnetar <= 3500)
	if id == 5002:
		return and_(IndustryIndex.qnetar >=3500, IndustryIndex.qnetar <= 4500)

	if id == 5003:
		return and_(IndustryIndex.qnetar >=4500, IndustryIndex.qnetar <= 5000)

	if id == 5004:
		return and_(IndustryIndex.qnetar >=5000, IndustryIndex.qnetar <= 5500)

	if id == 5005:
		return and_(IndustryIndex.qnetar >=5500, IndustryIndex.qnetar <= 6000)

	if id == 5006:
		return and_(IndustryIndex.qnetar >=6000, IndustryIndex.qnetar <= 7000)

	if id == 5007:
		return and_(IndustryIndex.qnetar >= 7000)

def St_filter(id):
	if id == 5011:
		return and_(IndustryIndex.star >= 0.0, IndustryIndex.star <= 0.5)

	if id == 5012:
		return and_(IndustryIndex.star >= 0.5, IndustryIndex.star <= 0.8)

	if id == 5013:
		return and_(IndustryIndex.star >= 0.8, IndustryIndex.star <= 1.0)

	if id == 5014:
		return and_(IndustryIndex.star >= 1.0)

def V_filter(id):
	if id == 5021:
		return and_(IndustryIndex.var >= 0.0, IndustryIndex.var <= 10.0)

	if id == 5022:
		return and_(IndustryIndex.var >= 10.0, IndustryIndex.var <= 20.0)

	if id == 5023:
		return and_(IndustryIndex.var >= 20.0, IndustryIndex.var <= 30.0)

	if id == 5024:
		return and_(IndustryIndex.var >= 30.0)

def Mt_filter(id):
	if id == 5031:
		return and_(IndustryIndex.mt >= 0.0, IndustryIndex.mt <= 10.0)

	if id == 5032:
		return and_(IndustryIndex.mt >= 10.0, IndustryIndex.mt <= 20.0)

	if id == 5033:
		return and_(IndustryIndex.mt >= 20.0, IndustryIndex.mt <= 30.0)

	if id == 5034:
		return and_(IndustryIndex.mt >= 30.0)


def main_chandi(fenlei=1):
	id_list_dict = {
		1: [622, 406, 4136, 1992, 4334, 3235, 5104, 5105, 5102, 5101],
		3: [406, 2197, 4588, 3561, 622, 5100, 5102], 
		2: [406, 1036, 1992, 5101]
	}
	id_list = id_list_dict[fenlei]
	chandi_list = map(lambda id: profile.get_chandi_setting_by_id(id), id_list)
	chandi_dict = [{'name': setting.getName(), 'url': url_for('main.stock', chandi=setting.id, fenlei=fenlei)} for setting in chandi_list]
	return chandi_dict

def main_Qnet(fenlei=1):
	id_list = [i+5000 for i in range(1, 8)]
	Qnet_list = map(lambda id: profile.get_Qnet_setting_by_id(id), id_list)
	Qnet_dict = [{'name': setting.getName(), 'url': url_for('main.stock', Qnet=setting.id, fenlei=fenlei)} for setting in Qnet_list]
	return Qnet_dict

def main_St(fenlei=1):
	id_list = [i+5010 for i in range(1, 5)]
	St_list = map(lambda id: profile.get_St_setting_by_id(id), id_list)
	St_dict = [{'name': setting.getName(), 'url': url_for('main.stock', St=setting.id, fenlei=fenlei)} for setting in St_list]
	return St_dict

def main_Mt(fenlei=1):
	id_list = [i+5030 for i in range(1, 5)]
	Mt_list = map(lambda id: profile.get_Mt_setting_by_id(id), id_list)
	Mt_dict = [{'name': setting.getName(), 'url': url_for('main.stock', Mt=setting.id, fenlei=fenlei)} for setting in Mt_list]
	return Mt_dict
