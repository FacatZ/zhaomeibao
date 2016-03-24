from . import api
from flask import render_template, request, url_for, jsonify
from ..models import User, ProductInformation, Category
from sqlalchemy import and_, or_
from sqlalchemy.exc import IntegrityError
from flask.ext.login import current_user, login_required
from ..decorators import admin_required
from ..models import ArticleCategory, Article
from ..util import data 
from ..database import db_session

@api.route('/<coalType>/<int:areaid>')
def get_coal_type_by_area_id(coalType, areaid):
	page = request.args.get('page', 1, type=int)
	count = request.args.get('count', 10, type=int)
	try:
		productInfo = ProductInformation.query.order_by(ProductInformation.timestamp.desc()) \
						.join(Category, Category.name == coalType) \
						.filter(ProductInformation.areaid==areaid) \
						.all()#.offset((page-1)*count).limit(count)

		print productInfo

		if not productInfo:
			return jsonify({'statecode': 404})

		return jsonify({
			'statecode':200,
			'info': [ product.to_brief_json() for product in productInfo]
			})
	except Exception, e:
		print e
		return jsonify({'statecode': 404})

#api below belong to admin account
@api.route('/admin/create/article', methods=['POST'])
@login_required
@admin_required
def admin_create_article():
	# print request.form
	# return jsonify({'statecode': 200})
	title = request.form.get('title', '', type=str)
	body = request.form.get('body', '', type=str)
	ctgid = request.form.get('ctgid', 1, type=int)
	# ctgid = int(ctgid)
	ac = ArticleCategory.query.filter_by(id=ctgid).first()
	if not ac:
		return jsonify({'statecode': 406})
	user = current_user._get_current_object()
	a = Article(title=title, body=body, category=ac, author=user)
	db_session.add(a)
	try:
		db_session.commit()
	except Exception, e:
		db_session.rollback()
		return jsonify({'statecode': 406})
	return jsonify({'statecode': 200})

@api.route('/admin/delete/article/<int:id>')
@login_required
@admin_required
def admin_delete_article(id):
	article = Article.query.filter_by(id=id).first()
	if not article:
		return jsonify({'statecode': 404})
	db_session.delete(article)
	try:
		db_session.commit()
		return jsonify({'statecode': 200})
	except Exception, e:
		db_session.rollback()
		return jsonify({'statecode': 406})

@api.route('/admin/publish/product', methods=['POST'])
@login_required
@admin_required
def admin_publish_product():
	# print request.form
	indIndex = data.processingIndustrialIndex()
	user = current_user._get_current_object()
	productInfo = data.processingProductInformation()
	category = data.processingCategory()
	# print category
	# print indIndex
	# print productInfo
	productInfo.user = user
	productInfo.industryIndex = indIndex
	productInfo.category = category
	db_session.add_all([indIndex, productInfo])
	# return jsonify({'statecode': 200})
	try:
		db_session.commit()
		return jsonify({'statecode': 200})
	except Exception, e:
		db_session.rollback()
		return jsonify({'statecode': 406})

@api.route('/admin/delete/product/<int:id>')
@login_required
@admin_required
def admin_delete_product(id):
	productInfo = ProductInformation.query.filter_by(id=id).first()
	indIndex = productInfo.industryIndex
	db_session.delete(productInfo)
	db_session.delete(indIndex)
	try:
		db_session.commit()
		return jsonify({'statecode': 200})
	except Exception, e:
		db_session.rollback()
		return jsonify({'statecode': 406})

@api.route('/admin/modify/product/<int:id>')
@login_required
@admin_required
def admin_modify_product(id):
	product = ProductInformation.query.filter_by(id=id).first()
	if not product:
		return jsonify({'statecode': 404})
	res = data.processingModifyProductInformation(product)
	if res:
		try:
			db_session.commit()
			return jsonify({'statecode': 200})
		except Exception, e:
			db_session.rollback()
	return jsonify({'statecode': 406})
# @api.route('/admin/get/article/list'):
# @login_required
# @admin_required
# def admin_get_article_list():
# 	return jsonify({'statecode': 200})

# @api.route('/admin/get/product/list')
# @login_required
# @admin_required
# def admin_get_product_list():
# 	return jsonify({'statecode': 200})


