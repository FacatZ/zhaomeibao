from app import create_app
from app.database import db_session
from flask.ext.script import Manager, Shell
# from app.models import User
from app.database import db_session, init_db, generate_fake_articles
from app.util import resources
from app.models import User, ProductInformation, Category, IndustryIndex, ArticleCategory, Article

app = create_app('development')
manager = Manager(app)

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
    		generate_fake_articles=generate_fake_articles)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
