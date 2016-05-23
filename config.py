

class Config:

	SECRET_KEY = 'CC61ivanBNYfwWBzXCgQLr0DSb9eXKia'

class DevelopmentConfig(Config):

	DEBUG = True

class ProductConfig(Config):
	DEBUG = False

	MAIL_USERNAME = '' #sender email to login xxxx@xxx.com
	MAIL_PASSWORD = '' #sender email password to login xxxxx

	MAIL_SERVER = '' # smtp server smtp.xxx.com
	MAIL_PORT = 587 # smtp port 587 or others

	ADMINS = ['']   #receiver email list ['xxxx@xxxx.com']
	MAIL_SENDER = MAIL_USERNAME 

	


config = {
	'development': DevelopmentConfig,
	'product': ProductConfig
}