from flask import request, render_template, flash, redirect, url_for, make_response
from flask import current_app as app
from .forms import LoginForm, SearchForm
from .models import db, User, Restaurant




@app.route('/')
@app.route('/index')

def index():
	search = SearchForm()
	user = {"username": "Sally"}
	return render_template('index.html', title="Home", user=user, search=search)


@app.route('/login', methods=['GET','POST'])
def login():
	search = SearchForm()
	form = LoginForm()
	if form.validate_on_submit():

		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		user = form.username.data
		new_restaurant = Restaurant(r_name= user,
									password_hash = "random password")
		db.session.add(new_restaurant)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template('login.html', title='Sign In',form=form,search=search)

@app.route("/user", methods=['GET', 'POST'])
def create_user():
	username = request.args.get('user')
	email = request.args.get('email')
	if username and email:
		new_user = User(username = username,
						email = email,
						created = dt.now(),
						bio= "rando bio",
						admin = False)
		db.session.add(new_user)
		db.session.commit()
	return make_response("successfully created!")

@app.route('/account')
def account():
	search = SearchForm()
	ip_request = requests.get('https://get.geojs.io/v1/ip.json')
	my_ip = ip_request.json()['ip'] 

	geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
	geo_request = requests.get(geo_request_url)
	geo_data = geo_request.json()
	print(geo_data)
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
	return render_template('account.html', title="Account", items=items, user=user, geo_data=geo_data, search=search)