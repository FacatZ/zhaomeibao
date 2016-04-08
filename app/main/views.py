from . import main
from flask import render_template, request, redirect, url_for
from ..models import ArticleCategory, Article, ProductInformation, Category
from sqlalchemy import and_
from ..util import data

@main.route('/')
def index():
	activeid = 0
	return render_template('main.html', activeid=activeid)

@main.route('/stock')
def stock():
	activeid = 1

	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 20, type=int)
	
	category = Category.query.all()
	product = ProductInformation.query.filter_by(typeid = 0).offset((page-1)*count).limit(count);
	producingArea = data.getStockProducingArea()
	jiaogeArea = data.getStockJiaogeArea()

	Qnet = data.getStockQnet()
	St = data.getStockSt()
	V = data.getStockV()
	Mt = data.getStockMt()
	
	return render_template('stock.html', activeid=activeid, category=category,
		product=product, producingArea=producingArea, 
		jiaogeArea=jiaogeArea, Qnet=Qnet, St=St,
		V=V, Mt=Mt)

	
@main.route('/purchase')
def purchase():
	activeid = 2
	return render_template('purchase.html', activeid=activeid)


@main.route('/logistics')
def logistics():
	activeid = 3
	return render_template('logistics.html', activeid=activeid)

@main.route('/spot_quotation')
def spot_quotation():
	activeid = 4
	actgid = request.args.get('type', 1, type=int)
	categorylist = ArticleCategory.query.all()
	category = ArticleCategory.query.filter_by(id=actgid).first()
	articles = category.articles.all()
	print actgid
	for a in articles:
		print a.title
	return render_template('spot-quotation.html', categorylist=categorylist, actgid=actgid, articles=articles, activeid=activeid)

@main.route('/detail/<int:id>')
def detail(id):
	product = ProductInformation.query.filter_by(id=id).first()
	if not product:
		return redirect(request.args.get('next') or url_for('main.index'))
	return render_template('details.html')