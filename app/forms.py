from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SearchForm(FlaskForm):
	searchParam = StringField(validators=[DataRequired()], description='Search restaurants or items')
	distanceRadius = FloatField(default = 0, description='e.g. 3')

class SignupForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email Address', validators=[DataRequired()])
	password = PasswordField('Password', validators=[
		DataRequired(),
		EqualTo('confirm', message='Passwords must match')]
		)
	confirm = PasswordField('Repeat Password')
	restaurantConf = BooleanField('Restaurant Account?')
	acceptTerms = BooleanField('I accept the Terms of Service and Privacy', validators=[DataRequired()])
	submit = SubmitField('Sign In')