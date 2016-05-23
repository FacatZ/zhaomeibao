#coding=utf-8
from sqlalchemy import create_engine
from flask import current_app
# engine = create_engine('sqlite:///test.db', convert_unicode=True, echo=False)
engine = create_engine('sqlite:///product.db', convert_unicode=True, echo=False)

from sqlalchemy.orm import scoped_session, sessionmaker
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
Base.query = db_session.query_property()

	
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



	for coalname in [u'动力煤', u'炼焦煤', u'无烟煤', u'焦炭/兰炭', u'生物质碳']:
		m = models.Category(name=coalname)
		db_session.add(m)
	try:
		db_session.commit()
	except Exception, e:
		db_session.rollback()
		print 'init coal category failed'

	#create an admin count
	#generate_fake_articles()