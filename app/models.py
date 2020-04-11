from app import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first = db.Column(db.String(64), index=True, unique=True)
    last = db.Column(db.String(400), unique=True)

class Restaurant(db.Model):
    id = db. Column(db.Integer, primary_key = True)
    r_name = db.Column(db.String(64), index=True, unique=True)
    r_address = db.Column(db.String(400), unique=True)
    phone = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    items = db.relationship('Item', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.r_name)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    i_name = db.Column(db.String(100))
    i_description = db.Column(db.String(200))
    i_price = db.Column(db.Float(10))
    i_quantity = db.Column(db.Integer)
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.id') )

def __repr__(self):
    return '<Item {}>'.format(self.body)