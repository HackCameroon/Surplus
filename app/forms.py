from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SearchForm(FlaskForm):
	searchParam = StringField(validators=[DataRequired()], description='Search Restaurants')
	zipcode = IntegerField(default = 0, description='e.g. 90007')

class SignupForm(FlaskForm):
	restaurant_email = StringField('Email', validators=[DataRequired()])
	restaurant_password = PasswordField('Password', validators=[
		DataRequired(),
		EqualTo('confirm', message='Passwords must match')]
		)
	confirm = PasswordField('Confirm')
	restaurant_name = StringField('Name of Business', validators=[DataRequired()])
	restaurant_phone = IntegerField('Phone Number', validators=[DataRequired()])
	restaurant_street = StringField('Street Address', validators=[DataRequired()])
	restaurant_city = StringField('City', validators=[DataRequired()])
	restaurant_state = StringField('State', validators=[DataRequired()])
	restaurant_zipcode = IntegerField('Zipcode', validators=[DataRequired()])
	submit = SubmitField('Sign Up')