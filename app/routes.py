from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, SearchForm
import requests



@app.route('/')
@app.route('/index')

def index():
	search = SearchForm()
	user = {"username": "Sally"}
	return render_template('index.html', title="Home", user=user, search=search)


@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In',form=form)

@app.route('/account')
def account():
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
	return render_template('account.html', title="Account", items=items, user=user, geo_data=geo_data)