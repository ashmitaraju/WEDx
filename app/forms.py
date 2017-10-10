from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired

class LoginForm(Form):
    username = StringField('username', validators =[DataRequired()])
    password = PasswordField('password', validators = [InputRequired()])
