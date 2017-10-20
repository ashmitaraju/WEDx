from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, TextField, ValidationError
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo, Required
from .models import Users

class LoginForm(Form):
    email = StringField('email', validators =[DataRequired(), Email()])
    password = PasswordField('password', validators = [InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(Form):
    email = StringField('E-Mail', validators = [InputRequired(), Email()])
    username = StringField('Username', validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [InputRequired(), EqualTo('confirm_password')])


    submit = SubmitField('Register')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use')

    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use')


class EditProfileForm(Form):

    genderChoices = [('male', 'Male'),('female', 'Female')]

    first_name = StringField('First Name', validators = [InputRequired()])
    last_name = StringField('Last Name', validators = [InputRequired()])
    gender = SelectField('Gender', choices = genderChoices, validators = [Required()])
    dob = DateField('Date of Birth', validators = [InputRequired()])
    hometown = StringField('Hometown', validators = [InputRequired()])
    mother_tongue = StringField('Mother Tongue', validators = [InputRequired()])
    about = TextField('About', validators = [InputRequired()])

    submit = SubmitField('Save Changes')
