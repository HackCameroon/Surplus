import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	TESTING = os.environ.get('TESTING')
	#FLASK_DEBUG = environ.get('FLASK_DEBUG')
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = True
