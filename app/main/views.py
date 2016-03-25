from . import main
from flask import render_template, request
from ..models import ArticleCategory, Article

@main.route('/')
def index():
	activeid = 0
	return render_template('main.html', activeid=activeid)

@main.route('/stock')
def stock():
	activeid = 1
	return render_template('stock.html', activeid=activeid)

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