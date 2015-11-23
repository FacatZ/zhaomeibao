

class Config:

	SECRET_KEY = 'hard to guess string'

class DevelopmentConfig(Config):

	DEBUG = True
	DB_PATH = 'sqlite:///test.db'

class ProductConfig(Config):
	DEBUG = False
	DB_PATH = ''  #None for now

config = {
	'development': DevelopmentConfig,
	'product': ProductConfig
}