from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {"username": "Sally"}
	return render_template('index.html', title="Home", user=user)

@app.route('/login')
def login():
	return render_template('account.html', title="Login")