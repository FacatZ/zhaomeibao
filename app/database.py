from sqlalchemy import create_engine
from flask import current_app
engine = create_engine('sqlite:///test.db', convert_unicode=True, echo=False)

from sqlalchemy.orm import scoped_session, sessionmaker
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	import models
	Base.metadata.create_all(engine)