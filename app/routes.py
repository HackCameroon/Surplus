
from flask import request, render_template, flash, redirect, url_for, make_response, session
from flask import current_app as app
from app.forms import LoginForm, SearchForm, SignupForm, AddItemForm
from app.models import db, seller, Inventory
from werkzeug.security import generate_password_hash, check_password_hash


db.create_all()

@app.route('/')
@app.route('/index')
def index():
	search = SearchForm()
	if session.get('logged_in') == True:
		user_id = session.get('user_id')
		name = seller.query.filter_by(seller_id=user_id).first().seller_name
		user = {"username": name}
	else:
		user = {"username": "Customer!"}
	return render_template('index.html', title="Home", user=user)

#sally is the best friend EVER
@app.route('/login', methods=['GET','POST'])
def login():
	search = SearchForm()
	if session.get('logged_in') == True:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():

		user = seller.query.filter_by(seller_email=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		session["user_id"] = user.seller_id
		session["logged_in"] = True
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In',form=form,search=search)

@app.route('/signup', methods=['GET','POST'])
def signup():
	search = SearchForm()
	if session.get('logged_in') == True:
		return redirect(url_for('index'))
	form = SignupForm()
	if form.validate_on_submit():
			name = form.restaurant_name.data
			email = form.restaurant_email.data
			phone = form.restaurant_phone.data
			zipcode = form.restaurant_zipcode.data
			address = form.restaurant_street.data + form.restaurant_city.data + form.restaurant_state.data
			new_seller = seller(
								seller_name=name,
								seller_email= email,
								seller_phone=phone,
								seller_zipcode=zipcode,
								seller_address=address
				)
			new_seller.set_password(form.restaurant_password.data)
			db.session.add(new_seller)
			db.session.commit()
			return redirect(url_for('index')) 

	return render_template('signup.html', title='Sign Up', form=form, search=search)

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/add', methods=['GET','POST'])
def additem():
	form = AddItemForm()
	search = SearchForm()


	current_user = seller.query.filter_by(seller_id = session.get('user_id')).first()
	
	if form.validate_on_submit():
			itemname = form.itemname.data
			itemquantity = form.itemquantity.data
			itemprice = form.itemprice.data
			itemdescription = form.itemdescription.data

			item = Inventory(item_name=itemname, item_price=itemprice, item_quantity = 1, item_image = "dolater.jpg", item_description = itemdescription, seller=current_user)
			item2 = Inventory(item_name=itemname, item_price=itemprice, item_quantity = 1, item_image = "dolater.jpg", item_description = itemdescription, seller=current_user)
		
			items = [item, item2]
			
			db.session.add(item)
			db.session.commit()
			#return redirect('/account')
			#return render_template('account.html',data=Inventory.query.all(), user=current_user)
			return redirect(url_for('account'))

			
	return render_template('add.html', title="Add", form=form, search=search, user=current_user)


@app.route('/account')
def account():




	search = SearchForm()

	## Code to add an item to a seller's inventory
	current_user = seller.query.filter_by(seller_id = session.get('user_id')).first()
	name = "my cool dinner"
	##


	##get duplicate results so we can add to quantity instead of adding another exact item
	duplicate_results = Inventory.query.filter(Inventory.item_name == name).join(seller).filter(seller.seller_id == current_user.seller_id).all()
	## need to do the quantity thing
	for result in duplicate_results:
		pass




	results = Inventory.query.join(seller).filter(seller.seller_id == current_user.seller_id).all()
	items_array = []
	items = current_user.items
	for item in results:
		item = {
				'name': item.item_name,
				'price': item.item_price,
				'quantity': item.item_quantity,
				'description': item.item_description
		}
		items_array.append(item)

	item_array = [
				{
					'name': 'margarita mix', 
					'price': 5.00,
					'quantity': 3,
					'description': "testdescription"
				},
				{
					'name': 'chicken soup',
					'price': 2.00,
					'quantity': 3,
					'description': "testdescription" 
				}, 
				{
					'name': 'beans',
					'price': 16.00,
					'quantity': 3,
					'description': "testdescription"
				}, 
				{
					'name': 'that one hot waiter',
					'price': 0.00,
					'quantity': 3,
					'description': "testdescription"
				} 
			]
	return render_template('account.html', title="Account", items=items_array, user=current_user, search=search)
