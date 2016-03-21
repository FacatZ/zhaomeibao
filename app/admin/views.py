from . import admin
from ..decorators import admin_required
from flask import render_template, redirect, request
from ..models import Article, User


@admin.route('/article/list')
#@admin_required
def article_list():
	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 10, type=int)
	articles = Article.query.offset((page-1)*count).limit(count)
	total = Article.query.count()
	return render_template('back-articles.html', articles=articles)

@admin.route('/create/article')
#@admin_required
def create_article():
	return render_template('back-issue.html', article=None)

@admin.route('/modify/article/<int:id>')
#@admin_required
def modify_article(id):
	article = Article.query.filter_by(id=id).first()
	if not article:
		return redirect('admin.article_list')
	return render_template('back-issue.html', article=article)