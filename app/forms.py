from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField, Form, SelectField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

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

class AddItemForm(FlaskForm):
	itemname = StringField('Item Name', validators=[DataRequired()])
	itemquantity = IntegerField('Quantity', validators=[DataRequired()])
	itemprice = FloatField("Price", validators=[DataRequired()])
	#itempicture = do this later
	itemdescription = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Add')

class EditItemForm(FlaskForm):
	itemname = StringField('Item Name', validators=[DataRequired()])
	itemquantity = IntegerField('Quantity', validators=[DataRequired()])
	itemprice = FloatField("Price", validators=[DataRequired()])
	#itempicture = do this later
	itemdescription = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Update Item')

class SearchForm(FlaskForm):
	searchParam = StringField('search', [DataRequired()])
	submit = SubmitField('Go', render_kw={'class': 'btn btn-success'})