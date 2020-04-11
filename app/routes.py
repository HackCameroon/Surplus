from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
@app.route('/index')

def index():
	user = {"username": "Sally"}
	return render_template('index.html', title="Home", user=user)


@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In',form=form)

@app.route('/account')
def account():
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
	return render_template('account.html', title="Account", items=items, user=user)