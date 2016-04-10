from . import main
from flask import render_template, request, redirect, url_for
from ..models import ArticleCategory, Article, ProductInformation, Category, IndustryIndex
from sqlalchemy import and_, or_
from ..util import data
from ..database import db_session

@main.route('/')
def index():
	activeid = 0

	categorylist = Category.query.limit(3)

	c = categorylist[0]
	dongli_huadong = c.productInformation.filter_by(dpareaid=1).order_by(ProductInformation.rldate.desc()).limit(15)
	dongli_huadong = [p.to_brief_json() for p in dongli_huadong]

	c = categorylist[0]
	dongli_huabei = c.productInformation.filter_by(dpareaid=2).order_by(ProductInformation.rldate.desc()).limit(15)
	dongli_huabei = [p.to_brief_json() for p in dongli_huabei]

	c = categorylist[0]
	dongli_huanan = c.productInformation.filter_by(dpareaid=7).order_by(ProductInformation.rldate.desc()).limit(15)
	dongli_huanan = [p.to_brief_json() for p in dongli_huanan]

	c = categorylist[0]
	dplist = [3, 4, 5, 6, 8]
	filter_result = reduce(or_, [ProductInformation.dpareaid == i for i in dplist])

	dongli_other = c.productInformation.filter(filter_result).order_by(ProductInformation.rldate.desc()).limit(15)
	dongli_other = [p.to_brief_json() for p in dongli_other]

	c = categorylist[1]
	wuyan_all = c.productInformation.order_by(ProductInformation.rldate.desc()).limit(15)
	wuyan_all = [p.to_brief_json() for p in wuyan_all]

	c = categorylist[2]
	lianjiao_all = c.productInformation.order_by(ProductInformation.rldate.desc()).limit(15)
	lianjiao_all = [p.to_brief_json() for p in lianjiao_all]

	article = Article.query.order_by(Article.hits.desc()).limit(10)

	return render_template('main.html', activeid=activeid, dongli_huadong=dongli_huadong,
				dongli_huabei=dongli_huabei, dongli_huanan=dongli_huanan, dongli_other=dongli_other,
				wuyan_all=wuyan_all, lianjiao_all=lianjiao_all, article=article)

@main.route('/stock')
def stock():
	activeid = 1

	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 20, type=int)
	
	category = Category.query.all()
	product = ProductInformation.query.filter_by(typeid = 1).order_by(ProductInformation.rldate.desc()).all()

	product_raw_all_filter = [ProductInformation.typeid == 1]
	#fen lei filter
	fenlei_query_string = request.args.get('fenlei', '', type=str)
	if fenlei_query_string != '':
		fenlei_list = fenlei_query_string.split(',')
		fenlei_filter = reduce(or_, [ProductInformation.ctgid == int(i) for i in fenlei_list])
		product_raw_all_filter.append(fenlei_filter)
	else:
		fenlei_query_string = None

	#chan di filter
	chandi_query_string = request.args.get('chandi', '', type=str)
	if chandi_query_string != '':
		chandi_list = chandi_query_string.split(',')
		chandi_filter = reduce(or_, [ProductInformation.pdpid == int(i) for i in chandi_list])
		product_raw_all_filter.append(chandi_filter)
	else:
		chandi_query_string = None

	#jiaogedi filter
	jiaogedi_query_string = request.args.get('jiaogedi', '', type=str)
	if jiaogedi_query_string != '':
		jiaogedi_list = jiaogedi_query_string.split(',')
		jiaogedi_filter = reduce(or_, [ProductInformation.dpareaid == int(i) for i in jiaogedi_list])
		product_raw_all_filter.append(jiaogedi_filter)
	else:
		jiaogedi_query_string = None

	#join query
	industryIndex_raw_all_filter = [ProductInformation.indid == IndustryIndex.id]
	#Qnet filter
	Qnet_query_string = request.args.get('Qnet', '', type=str)
	if Qnet_query_string != '':
		Qnet_list = Qnet_query_string.split(',')
		Qnet_filter = reduce(or_, [data.Qnet_filter(int(id)) for id in Qnet_list])
		industryIndex_raw_all_filter.append(Qnet_filter)
	else:
		Qnet_query_string = None

	#St filter
	St_query_string = request.args.get('St', '', type=str)
	if St_query_string != '':
		St_list = St_query_string.split(',')
		St_filter = reduce(or_, [data.St_filter(int(id)) for id in St_list])
		industryIndex_raw_all_filter.append(St_filter)
	else:
		St_query_string = None

	#V filter
	V_query_string = request.args.get('V', '', type=str)
	if V_query_string != '':
		V_list = V_query_string.split(',')
		V_filter = reduce(or_, [data.V_filter(int(id)) for id in V_list])
		industryIndex_raw_all_filter.append(V_filter)
	else:
		V_query_string = None

	#Mt filter
	Mt_query_string = request.args.get('Mt', '', type=str)
	if Mt_query_string != '':
		Mt_list = Mt_query_string.split(',')
		Mt_filter = reduce(or_, [data.Mt_filter(int(id)) for id in Mt_list])
		industryIndex_raw_all_filter.append(Mt_filter)
	else:
		Mt_query_string = None

	product_all_filter = reduce(and_, product_raw_all_filter)
	industryIndex_all_filter = reduce(and_, industryIndex_raw_all_filter)

	pagination = data.Pagination(ProductInformation.query.join(IndustryIndex, industryIndex_all_filter).filter(product_all_filter).order_by(ProductInformation.rldate.desc()),\
				page, count)
	product = pagination.items

	producingArea = data.getStockProducingArea()
	jiaogeArea = data.getStockJiaogeArea()

	Qnet = data.getStockQnet()
	St = data.getStockSt()
	V = data.getStockV()
	Mt = data.getStockMt()
	
	return render_template('stock.html', activeid=activeid, category=category,
		product=product, producingArea=producingArea, 
		jiaogeArea=jiaogeArea, Qnet=Qnet, St=St,
		V=V, Mt=Mt, pagination=pagination, count=count, fenlei_query_string=fenlei_query_string, chandi_query_string=chandi_query_string,
		jiaogedi_query_string=jiaogedi_query_string, Qnet_query_string=Qnet_query_string,
		St_query_string=St_query_string, V_query_string=V_query_string, Mt_query_string=Mt_query_string)

	
@main.route('/purchase')
def purchase():
	activeid = 2
	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 6, type=int)
	pagination = data.Pagination(ProductInformation.query.filter_by( typeid = 0).order_by(ProductInformation.rldate.desc()), page, count)
	product = pagination.items
	return render_template('purchase.html', activeid=activeid, product=product,
				 count=count, pagination=pagination)


@main.route('/logistics')
def logistics():
	activeid = 3
	return render_template('logistics.html', activeid=activeid)

@main.route('/spot_quotation')
def spot_quotation():
	activeid = 4
	actgid = request.args.get('type', 1, type=int)

	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 20, type=int)

	categorylist = ArticleCategory.query.all()
	category = ArticleCategory.query.filter_by(id=actgid).first()

	pagination = data.Pagination(Article.query.filter_by(ctgid=actgid).order_by(Article.rldate.desc()), page, count)
	articles = pagination.items
	
	return render_template('spot-quotation.html', categorylist=categorylist, type=actgid, 
				articles=articles, activeid=activeid, pagination=pagination, count=count)

@main.route('/detail/<int:id>')
def detail(id):
	product = ProductInformation.query.filter_by(id=id).first()
	if not product:
		return redirect(request.args.get('next') or url_for('main.index'))
	return render_template('details.html', pd=product)

@main.route('/article/<int:id>')
def article(id):
	article = Article.query.filter_by(id=id).first()
	if not article:
		return redirect(url_for('main.spot_quotation'))
	article.hits += 1
	db_session.add(article)
	db_session.commit()
	return render_template('details-article.html', article=article)