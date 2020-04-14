
from flask import request, render_template, flash, redirect, url_for, make_response, session
from flask import current_app as app
from app.forms import LoginForm, SearchForm, SignupForm
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

@app.route('/account')
def account():
	search = SearchForm()
	current_user = seller.query.filter_by(seller_id = session.get('user_id')).first()
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
	return render_template('account.html', title="Account", items=items, user=current_user, search=search)
