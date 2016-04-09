#coding=utf-8
from sqlalchemy import create_engine
from flask import current_app
engine = create_engine('sqlite:///test.db', convert_unicode=True, echo=False)

from sqlalchemy.orm import scoped_session, sessionmaker
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
Base.query = db_session.query_property()

def generate_fake_articles():
	import models
	admin = models.User.query.filter_by(username='admin').first()
	if not admin:
		print 'no admin'
		return 

	titlelist = [u'标题1',u'标题2',u'标题3',u'标题4']
	bodylist = [u'内容1',u'内容2',u'内容3',u'内容4',]
	for title, body in zip(titlelist, bodylist):
		a = models.Article(title=title, body=body)
		res = admin.create_article(a)

		from random import randint
		acId = randint(0, 4)
		articleCategory = models.ArticleCategory.query.filter_by(id=acId).first()
		a.category = articleCategory
		db_session.commit()
		if not res:
			print 'init articles %s failed' %(title)
	
def init_db():
	import models
	Base.metadata.create_all(engine)
	for Aname in [u'煤市行情', u'煤市资讯', u'物流仓库', u'指数及指标']:
		m = models.ArticleCategory(name=Aname)
		db_session.add(m)
	try:
		db_session.commit()
	except Exception, e:
		db_session.rollback()
		print 'init articles category failed'

	import datetime
	for i in range(0,2):
		today = datetime.date.today()
		count = 0
		order = models.OrderNumberRecord.query.filter_by(pdtype=i).first()
		if not order:
			order = models.OrderNumberRecord()
		order.last_date = today
		order.count = count
		order.pdtype = i
		db_session.add(order)
		try:
			db_session.commit()
		except:
			db_session.rollback()
			print 'init OrderNumberRecord type %d table error' %(i)


	for coalname in [u'动力煤', u'炼焦煤', u'无烟煤', u'焦炭/兰炭', u'生物质碳']:
		m = models.Category(name=coalname)
		db_session.add(m)
	try:
		db_session.commit()
	except Exception, e:
		db_session.rollback()
		print 'init coal category failed'

	#create an admin count
	admin = models.User(username='admin', password='admin', permissions=0xFF)
	db_session.add(admin)
	try:
		db_session.commit()
	except Exception, e:
		db_session.rollback()
		print 'create admin count failed'
	#generate_fake_articles()