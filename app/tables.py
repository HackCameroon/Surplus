from flask_table import Table, Col, LinkCol
class Results(Table):
    id = Col('Id', show=False)
    artist = Col('Artist')
    title = Col('Title')
    release_date = Col('Release Date')
    publisher = Col('Publisher')
    media_type = Col('Media')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))



seller_id = db.Column(db.Integer, db.ForeignKey('seller.seller_id'))
    item_name = db.Column(db.String)
    item_price = db.Column(db.String)
    item_quantity = db.Column(db.Integer)
    item_image = db.Column(db.String)
    item_description = db.Column(db.String)