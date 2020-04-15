import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

directoryPath = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directoryPath, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class seller(UserMixin, db.Model):
    seller_id = db.Column(db.Integer, primary_key=True)
    seller_email = db.Column(db.String, unique=True)
    seller_name = db.Column(db.String)
    seller_zipcode = db.Column(db.Integer)
    seller_phone = db.Column(db.Integer)
    seller_address = db.Column(db.String)
    password_hash = db.Column(db.String(128))
    items = db.relationship('Inventory', backref='seller')
    #def __init__(self, seller_email, seller_name, seller_zipcode, seller_phone, seller_address):
        #self.seller_email = seller_email
        #self.seller_name = seller_name
        #self.seller_zipcode = seller_zipcode
        #self.seller_phone = seller_phone
        #self.seller_address = seller_address

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Inventory(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.seller_id'))
    item_name = db.Column(db.String)
    item_price = db.Column(db.String)
    item_quantity = db.Column(db.Integer)
    item_image = db.Column(db.String)
    item_description = db.Column(db.String)
    #def __init__(self, seller_id, item_name, item_price, item_quantity, item_image, item_description):
        #self.seller_id = seller_id
        #self.item_name = item_name
        #self.item_price = item_price
        #self.item_quantity = item_quantity
        #self.item_image = item_image
        #self.item_description = item_description
