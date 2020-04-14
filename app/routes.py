
from flask import request, render_template, flash, redirect, url_for, make_response
from flask import current_app as app
from app.forms import LoginForm, SearchForm, SignupForm
from app.models import db, seller, Inventory
from werkzeug.security import generate_password_hash, check_password_hash



@app.route('/')
@app.route('/index')
def index():
	search = SearchForm()
	user = {"username": "Sally"}
	return render_template('index.html', title="Home", user=user)

#sally is the best friend EVER
@app.route('/login', methods=['GET','POST'])
def login():
	search = SearchForm()
	form = LoginForm()
	if form.validate_on_submit():

		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		user = form.username.data
		return redirect(url_for('index'))

	return render_template('login.html', title='Sign In',form=form,search=search)

@app.route('/signup', methods=['GET','POST'])
def signup():
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

	return render_template('signup.html', title='Sign Up', form=form)

@app.route('/account')
def account():
	search = SearchForm()
	current_user = "La Barca"
	inventory = Inventory.query.filter_by(Inventory.Seller(has (seller_name=current_user))).all()
	print(inventory)
	user = {"username": "La Barca"}
	items = [
				{
					'name': 'margarita mix', 
					'price': 5.00
				},
				{
					'name': 'chicken soup',
					'price': 2.00 
				}, 
				{
					'name': 'beans',
					'price': 16.00
				}, 
				{
					'name': 'that one hot waiter',
					'price': 0.00
				} 
			]
	return render_template('account.html', title="Account", items=items, user=user, search=search)