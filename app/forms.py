from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo
from .models import Users

class LoginForm(Form):
    email = StringField('email', validators =[DataRequired(), Email()])
    password = PasswordField('password', validators = [InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(Form):
    email = StringField('E-Mail', validators = [InputRequired()])
    username = StringField('Username', validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [InputRequired(), EqualTo('confirm_password')])
    first_name = StringField('First Name', validators = [InputRequired()])

    submit = SubmitField('Register')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use')

    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use')
