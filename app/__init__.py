from flask import Flask
from config import config
from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.login_view = 'member.login'

def create_app(configtype):
	app = Flask(__name__)
	app.config.from_object(config[configtype])

	login_manager.init_app(app)

	#define blueprint below
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint, url_prefix='/admin')

	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix='/api')
	
	return app