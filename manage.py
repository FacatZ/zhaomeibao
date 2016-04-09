#coding=utf-8
from app import create_app
from app.database import db_session
from flask.ext.script import Manager, Shell
# from app.models import User
from app.database import db_session, init_db, generate_fake_articles
from app.util import resources
from app.models import User, ProductInformation, Category, IndustryIndex, ArticleCategory, Article, OrderNumberRecord
from flask.ext.login import login_user
from app.util.location import location

app = create_app('development')
manager = Manager(app)


@app.template_filter('productInformation_typeid_filter')
def productInformation_typeid_filter(id):
	id = str(id)
	dd = {
		u'0': u'需求',
		u'1': u'供货'
	}
	return dd[id]

@app.template_filter('IndustryIndex_int_filter')
def IndustryIndex_int_filter(n):
	n = int(n)
	return '-' if not n or n == 0 or n == '' else '%d' %(n)

@app.template_filter('IndustryIndex_float_filter')
def IndustryIndex_float_filter(n):
	n = float(n)
	return '-' if (not n or n == 0.0 or n == '') else ('%.2f%%' %(n))

@app.template_filter('Qnet_filter')
def Qnet_filter(qnet):
	print 'qnet filter:', qnet
	l = []
	qnet = int(qnet)
	while qnet > 0:
		l.append(qnet % 1000)
		qnet /= 1000
	l = l[::-1]
	print (','.join([str(n) for n in l]))
	return u'0' if qnet is None or qnet == '' else (','.join([str(n) for n in l]))

@app.template_filter('rldate_filter')
def rldate_filter(rldate):
	return rldate.strftime('%Y-%m-%d %H:%M')

@app.template_filter('stock_filter')
def stock_filter(stock):
	return u'0' if not stock or stock == '' else stock

@app.template_filter('province_filter')
def province_filter(id):
	return location['0'][int(id)] if id else u'暂无'

@app.template_filter('pdtype_filter')
def pdtype_filter(id):
	dd = {
		'0': u'期货',
		'1': u'现货'
	}
	return dd[id]

@app.template_filter('prtype_filter')
def prtype_filter(s):
	return u'暂无价格类型' if not s or s == '' else s

@app.template_filter('string_filter')
def string_filter(s):
	return u'暂无' if not s or s == '' else s

@app.template_filter('dict_sorted')
def dict_sorted(s):
	return sorted(s)

@app.template_filter('setting_format')
def setting_format(s):
	return s.replace('-*', u'以上')


# @app.before_first_request
# def first_request_processor():
# 	admin = User.query.filter_by(username='admin').first()
# 	login_user(admin)

@app.teardown_appcontext
def teardown_database(exception=None):
	db_session.remove()

@app.context_processor
def city_filter_processor():
	def city_filter(pid, cid):
		pstring = '0'
		pstring = ','.join([pstring, str(pid)])
		if not location[pstring].has_key(cid):
			return u'暂无'
		return location[pstring][cid]
	return dict(city_filter=city_filter)

@app.context_processor
def datetime_format_processor():
	def format_datetime(date):
		if not date:
			return ''
		return str(date).split()[0]
	return dict(format_datetime=format_datetime)

@app.context_processor
def article_context_processor():
	def get_article_context_or_none(context):
		return context if context else ''
	return dict(get_article_context_or_none=get_article_context_or_none)

def make_shell_context():
    return dict(app=app, db_session=db_session, init_db=init_db, User=User, ProductInformation=ProductInformation, Category=Category, IndustryIndex=IndustryIndex, ArticleCategory=ArticleCategory, Article=Article, \
    		generate_fake_articles=generate_fake_articles, OrderNumberRecord=OrderNumberRecord)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
