from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
	app = Flask(__name__, instance_relative_config=False)
	app.run(debug=True)
	app.config.from_object(Config)
	db.init_app(app)
	#migrate = Migrate(app, db)
	with app.app_context():
		from app import routes, models
		db.create_all()
		return app


		




#from app import routes, models

#app = Flask(__name__)
#app.run(debug=True)

#app.config.from_object(Config)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#from app.models import Test, Restaurant
#print("HIIIIII")
#t = Test(first='Anna', last = 'SSSSSSS')
#print(t.last)

#r = Restaurant(r_name="Chanos", r_address="123 USC Rd", phone="(123)-456-7890", password_hash="fhlaksdjfhlaksjdhf" )
#print(r)
#db.session.add(r)
#db.session.commit()


#from app import routes, models