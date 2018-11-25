from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class SignupForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password_confirm', message='Passwords must match')])
    password_confirm = PasswordField(
        'Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("Account already exists")
