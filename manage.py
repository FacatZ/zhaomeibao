from app import create_app
from app.database import db_session
from flask.ext.script import Manager, Shell
# from app.models import User
from app.database import db_session, init_db

app = create_app('development')
manager = Manager(app)

@app.teardown_appcontext
def teardown_database(exception=None):
	db_session.remove()

def make_shell_context():
    return dict(app=app, db_session=db_session, init_db=init_db)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
