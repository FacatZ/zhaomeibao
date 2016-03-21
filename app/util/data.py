from app.models import User, ProductInformation, Category, IndustryIndex, ArticleCategory, Article
from sqlalchemy import and_
from flask import request

def getProductInformationByArea(areaId, num=10):
	return ProductInformation.query.filter_by(areaid=areaId).limit(num)

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
		'var': request.form.get('var'),
		'vad': request.form.get('vad'),
		'vdaf': request.form.get('vdaf'),
		'aar': request.form.get('aar'),
		'aad': request.form.get('aad'),
		'fcar': request.form.get('fcar'),
		'fcad': request.form.get('fcad'),
		'star': request.form.get('start'),
		'stad': request.form.get('stad'),
		'qnetar': request.form.get('qnetar'),
		'qnetad': request.form.get('qnetad'),
		'szuplm': request.form.get('szuplm'),
		'szlowlm': request.form.get('szlowlm'),
		'szppt': request.form.get('szppt')
	}



def processingIndustrialIndex():
	mt = request.form.get('mt')
	mt = float(mt)
	mad = request.form.get('mad')
	mad = float(mt)

	var = request.form.get('var')
	var = float(var)
	vad = request.form.get('vad')
	vad = float(vad)
	vdaf = request.form.get('vdaf')
	vdaf = float(vdaf)

	aar = request.form.get('aar')
	aar = float(aar)
	aad = request.form.get('aad')
	aad = float(aad)

	fcar = request.form.get('fcar')
	fcar = float(fcar)
	fcad = request.form.get('fcad')
	fcad = float(fcad)

	star = request.form.get('start')
	star = float(start)
	stad = request.form.get('stad')
	stad = float(stad)

	qnetar = request.form.get('qnetar')
	qnetar = int(qnetar)
	qnetad = request.form.get('qnetad')
	qnetad = int(qnetad)

	szuplm = request.form.get('szuplm')
	szuplm = int(szuplm)
	szlowlm = request.form.get('szlowlm')
	szlowlm = int(szlowlm)
	szppt = request.form.get('szppt')
	szppt = int(szppt)

	return IndustryIndex(mt=mt, mad=mad, var=var, vad=vad, vdaf=vdaf, \
			aar=aar, aad=aad, fcar=fcar, fcad=fcad, star=star, stad=stad, \
			qnetar=qnetar, qnetad=qnetad, szuplm=szuplm, szlowlm=szlowlm, szppt=szppt)

def processingProductInformation():

	typeid = request.form.get('typeid', 0, type=int)

	pdpid = request.form.get('pdpid', 1, type=int)
	pdcid = request.form.get('pdcid', 1, type=int)

	coal = request.form.get('coal', '', type=str)
	count = request.form.get('count', 0, type=int)
	price = request.form.get('price', 0.0, type=float)

	prtype = request.form.get('prtype', '', type=str)
	prpid = request.form.get('prpid', 1, type=int)
	prcid = request.form.get('prcid', 1, type=int)
	
	vldterm = request.form.get('vldterm', '', type=str)

	dppid = request.form.get('prpid', 1, type=int)
	dpcid = request.form.get('prcid', 1, type=int)
	dpaddr = request.form.get('dpaddr', '', type=str)

	paytype = request.form.get('paytype', '', type=str)
	remark = request.form.get('remark', '', type=str)

	return ProductInformation(typeid=typeid, pdpid=pdpid, pdcid=pdcid, \
			coal=coal, count=count, price=price, \
			prtype=prtype, prpid=prpid, prcid=prcid, vldterm=vldterm,\
			dppid=dppid, dpcid=dpcid, dpaddr=dpaddr,\
			paytype=paytype, remark=remark)

def processingCategory():
	cid = request.form.get('cid', 1, type=int)
	return Category.query.filter_by(id=cid).first()

def processingModifyProductInformation(product):
	
	return True