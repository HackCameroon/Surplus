from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.run(debug=True)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import Test, Restaurant
print("HIIIIII")
t = Test(first='Anna', last = 'SSSSSSS')
print(t.last)

# r = Restaurant(r_name="Chanos", r_address="123 USC Rd", phone="(123)-456-7890", password_hash="fhlaksdjfhlaksjdhf" )
# print(r)
# db.session.add(r)
# db.session.commit()


from app import routes, models