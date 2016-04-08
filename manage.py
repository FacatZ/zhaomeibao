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


@app.before_first_request
def first_request_processor():
	admin = User.query.filter_by(username='admin').first()
	login_user(admin)

@app.teardown_appcontext
def teardown_database(exception=None):
	db_session.remove()

@app.context_processor
def datetime_format_processor():
	def format_datetime(date):
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
