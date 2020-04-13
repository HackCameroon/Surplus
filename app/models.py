import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

directoryPath = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directoryPath, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Seller(db.Model):
    seller_id = db.Column(db.Integer, primary_key=True)
    seller_email = db.Column(db.String, unique=True)
    seller_name = db.Column(db.String)
    seller_password = db.Column(db.String)
    seller_zipcode = db.Column(db.Integer)
    seller_phone = db.Column(db.Integer)
    seller_address = db.Column(db.String)
    def __init__(self, seller_id, seller_email, seller_name, seller_password, seller_zipcode, seller_phone, seller_address):
        self.seller_id = seller_id
        self.seller_email = seller_email
        self.seller_name = seller_name
        self.seller_password = seller_password
        self.seller_zipcode = seller_zipcode
        self.seller_phone = seller_phone
        self.seller_address = seller_address

class Inventory(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, foreign_key=True)
    item_name = db.Column(db.String)
    item_price = db.Column(db.String)
    item_quantity = db.Column(db.Integer)
    item_image = db.Column(db.String)
    item_description = db.Column(db.String)
    def __init__(self, item_id, seller_id, item_name, item_price, item_quantity, item_image, item_description):
        self.item_id = item_id
        self.seller_id = seller_id
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_image = item_image
        self.item_description = item_description