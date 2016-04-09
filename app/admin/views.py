from . import admin
from ..decorators import admin_required
from flask import render_template, redirect, request, url_for
from ..models import Article, User, ProductInformation, ArticleCategory, Category
from flask.ext.login import login_required, logout_user, login_user
from ..util import data

@admin.route('/')
@admin.route('/product/list')
@login_required
@admin_required
def product_list():
	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 30, type=int)
	pagination = data.Pagination(ProductInformation.query, page, count)
	product = pagination.items
	return render_template('back-production.html', product=product)#, pagination=pagination)

@admin.route('/create/product')
@login_required
@admin_required
def create_product():

	category = Category.query.all()

	return render_template('back-publish.html', category=category)

@admin.route('/modify/product/<int:id>')
@login_required
@admin_required
def modify_product(id):
	product = ProductInformation.query.filter_by(id=id).first()
	if not product:
		return redirect(url_for('admin.product_list'))

	industryIndex = product.industryIndex
	category = Category.query.all()

	print 'before product'
	for k, v in vars(product).items():
		print '%s=%s' %(str(k), getattr(product, k, ''))


	return render_template('back-modify.html', category=category,\
		product=product, industryIndex=industryIndex)

@admin.route('/article/list')
@login_required
@admin_required
def article_list():
	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 10, type=int)
	pagination = data.Pagination(Article.query, page, count)
	articles = pagination.items
	# articles = Article.query.offset((page-1)*count).limit(count)
	# total = Article.query.count()
	return render_template('back-articles.html', count=count,articles=articles, pagination=pagination)

@admin.route('/create/article')
@login_required
@admin_required
def create_article():
	categorylist = ArticleCategory.query.all()
	return render_template('back-issue.html', categorylist=categorylist)

@admin.route('/modify/article/<int:id>')
@login_required
@admin_required
def modify_article(id):
	article = Article.query.filter_by(id=id).first()
	categorylist = ArticleCategory.query.all()
	if not article:
		return redirect('admin.article_list')
	return render_template('back-issue-modify.html', categorylist=categorylist, article=article)

@admin.route('/logout')
@login_required
@admin_required
def admin_logout():
	logout_user()
	return redirect( url_for('main.index'))

@admin.route('/login')
def admin_login():
	return render_template('login.html')