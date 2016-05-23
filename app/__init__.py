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

	if not app.debug and app.config['MAIL_SERVER'] != '':
		import logging
		from logging.handlers import SMTPHandler
		MAIL_SERVER = app.config['MAIL_SERVER']
		MAIL_SENDER = app.config['MAIL_SENDER']
		MAIL_PORT = app.config['MAIL_PORT']
		ADMINS = app.config['ADMINS']
		MAIL_USERNAME = app.config['MAIL_USERNAME']
		MAIL_PASSWORD = app.config['MAIL_PASSWORD']

		mail_handler = SMTPHandler( \
				mailhost=(MAIL_SERVER, MAIL_PORT), \
				fromaddr=MAIL_SENDER, \
				toaddrs=ADMINS, \
				subject='Application Error', \
				credentials=(MAIL_USERNAME, MAIL_PASSWORD), \
				secure=None)

		mail_handler.setLevel(logging.ERROR)
		app.logger.addHandler(mail_handler)

	#define blueprint below
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint, url_prefix='/admin')

	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix='/api')
	
	return app