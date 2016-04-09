#coding=utf-8
from . import api
from flask import render_template, request, url_for, jsonify, redirect
from ..models import User, ProductInformation, Category
from sqlalchemy import and_, or_
from sqlalchemy.exc import IntegrityError
from flask.ext.login import current_user, login_required, login_user
from ..decorators import admin_required
from ..models import ArticleCategory, Article
from ..util import data, profile
from ..database import db_session

@api.route('/admin/login', methods=['POST'])
def admin_login():
	username = request.form.get('name', '', type=str)
	password = request.form.get('password', '', type=str)
	print request.form
	user = User.query.filter_by( username=username).first()
	if not user:
		return jsonify({'statecode': 404})
	if user.verify_password(password):
		login_user(user)
		return jsonify({
				'statecode': 200,
				'url': url_for('admin.product_list')
			})
	return jsonify({'statecode': 406})


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
@api.route('/admin/get/article/<int:id>')
@login_required
@admin_required
def admin_get_article(id):
	article = Article.query.filter_by(id=id).first()
	if not article:
		return jsonify({'statecode': 404})
	return jsonify({
		'statecode': 200,
		'data': article.to_json()
		})

@api.route('/admin/create/article', methods=['POST'])
@login_required
@admin_required
def admin_create_article():
	title = request.form.get('title', '', type=unicode)
	body = request.form.get('body', '', type=unicode)
	#body = data.filterUserInput(body)
	ctgid = request.form.get('ctgid', 1, type=int)
	ac = ArticleCategory.query.filter_by(id=ctgid).first()
	if not ac:
		return redirect(url_for('admin.article_list'))
		# return jsonify({'statecode': 406})
	user = current_user._get_current_object()
	a = Article(title=title, body=body, category=ac, author=user)
	db_session.add(a)
	try:
		db_session.commit()
	except Exception, e:
		db_session.rollback()
		return redirect(url_for('admin.article_list'))
		# return jsonify({'statecode': 406})
	return redirect(url_for('main.article', id=a.id))

@api.route('/admin/modify/article/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_modify_article(id):
	article = Article.query.filter_by(id=id).first()
	if not article:
		return redirect(url_for('admin.article_list'))
	article_params_dict = data.preprocessingArticleDict()
	article.modify_from_dict(article_params_dict)
	db_session.add(article)
	try:
		db_session.commit()
		return redirect(url_for('main.article', id=article.id))
	except Exception, e:
		db_session.rollback()
		return redirect(url_for('admin.article_list'))

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

	indIndex = data.processingIndustrialIndex()
	productInfo = data.processingProductInformation()
	print '-----------'
	print indIndex
	print productInfo
	if not indIndex or not productInfo:
		return jsonify({'statecode': 406})
	user = current_user._get_current_object()
	category = data.processingCategory()

	productInfo.user = user
	productInfo.ordnum = data.generate_unique_serial_number(productInfo.typeid)
	productInfo.industryIndex = indIndex
	productInfo.category = category
	productInfo.dpareaid = profile.get_jiaoge_group_id_by_name(productInfo.dpaddr)
	db_session.add_all([indIndex, productInfo])
	try:
		db_session.commit()
		prid = productInfo.id
		return jsonify({
			'statecode': 200,
			'url': url_for('main.detail', id=prid) if productInfo.typeid == 1 else url_for('main.purchase')
			})
	except Exception, e:
		db_session.rollback()
		print e
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

@api.route('/admin/modify/product/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_modify_product(id):
	product = ProductInformation.query.filter_by(id=id).first()
	if not product:
		return jsonify({'statecode': 404})


	product_dict = data.preprocessingProductInformationModifyDict()
	product.modify_from_dict(product_dict)
	industry_dict = data.preprocessingIndutrialIndex()
	industryIndex = product.industryIndex
	industryIndex.modify_from_dict(industry_dict)

	db_session.add_all([product, industryIndex])
	try:
		db_session.commit()
		prid = product.id
		return jsonify({
					'statecode': 200,
					'url': url_for('main.detail', id=prid) if product.typeid == 1 else url_for('main.purchase') 
					})
	except Exception, e:
		db_session.rollback()
	return jsonify({'statecode': 406})


@api.route('/admin/get/product/<int:id>')
@login_required
@admin_required
def admin_get_product(id):
	product = ProductInformation.query.filter_by(id=id).first()
	indid = product.industryIndex
	if not product:
		return jsonify({'statecode': 404})
	return jsonify({
		'statecode': 200,
		'data': 
			{
				'product': product.to_json(),
				'industryIndex': indid.to_json()
			}
		})

@api.route('/admin/create/product')
@login_required
@admin_required
def admin_create_product():
	product_dict = data.preprocessingProductInformationDict()
	indid_dict = data.preprocessingIndutrialIndex()

	product = ProductInformation.from_dict(product_dict)
	indid = industryIndex.from_dict()

	product.industryIndex = indid
	db_session.add_all([product, indid])
	try:
		db_session.commit()
		return jsonify({
			'statecode': 200
			})
	except:
		db_session.rollback()
		return jsonify({
			'statecode': 406
			})

# @api.route('/admin/modify/product/<int:id>')
# @login_required
# @admin_required
# def admin_modify_product(id):
# 	product_dict = data.preprocessingProductInformationDict()
# 	indid_dict = data.preprocessingIndutrialIndex()

# 	product = ProductInformation.query.filter_by(id=id).first()
# 	if not product:
# 		return jsonify({
# 			'statecode': 404
# 			})

# 	indid = product.industryIndex

# 	product.modify_from_dict(product_dict)
# 	indid.modify_from_dict(indid_dict)
# 	# product.industryIndex = indid
# 	# db_session.add_all([product, indid])
# 	try:
# 		db_session.commit()
# 		return jsonify({
# 			'statecode': 200
# 			})
# 	except:
# 		db_session.rollback()
# 		return jsonify({
# 			'statecode': 406
# 			})
