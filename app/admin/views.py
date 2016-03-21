from . import admin
from ..decorators import admin_required
from flask import render_template, redirect, request
from ..models import Article, User, ProductInformation
from flask.ext.login import login_required
from ..util import data

@admin.route('/')
@admin.route('/product/list')
@login_required
@admin_required
def product_list():
	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 10, type=int)
	pagination = data.Pagination(ProductInformation.query, page, count)
	product = pagination.items
	return render_template('back-production.html', product=product)#, pagination=pagination)

@admin.route('/create/product')
@login_required
@admin_required
def create_product():
	return render_template('back-publish.html')

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
	return render_template('back-issue.html')

@admin.route('/modify/article/<int:id>')
@login_required
@admin_required
def modify_article(id):
	article = Article.query.filter_by(id=id).first()
	if not article:
		return redirect('admin.article_list')
	return render_template('back-issue-modify.html', article=article)