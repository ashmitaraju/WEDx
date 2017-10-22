from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField,  TextField, ValidationError , IntegerField
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo, Required
from wtforms.fields.html5 import DateField

from .models import *

from .models import Users
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images

class LoginForm(Form):
    email = StringField('E-mail', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
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
    current_location = StringField('Current Location' , validators = [InputRequired()])
    image = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    submit = SubmitField('Submit')

class EditEducationForm(Form):

    school = StringField('School')
    under_grad = StringField('Under Graduation')
    post_grad = StringField('Post Gradution')
    submit = SubmitField('Save Changes')

class EditEmploymentForm(Form):
     occupation = StringField('Occupation')
     designation = StringField('Designation')
     company_name = StringField('Company Name')
     salary = IntegerField('Salary')
     submit = SubmitField('Save Changes')

class EditPreferencesForm(Form):

    genderChoices = [('male', 'Male'),('female', 'Female')]

    occupation = StringField('Occupation')
    salary = IntegerField('Salary')
    hometown = StringField('Hometown')
    height = IntegerField('Height')
    current_location = StringField('Current Location')
    gender = SelectField('Gender', choices = genderChoices)
    mother_tongue = StringField('Mother Tongue')
    about = TextField('About')
    submit = SubmitField('Save Changes')

class EditSocialMediaForm(Form):

    facebook = StringField('Facebook Link')
    twitter = StringField('Twitter Link')
    instagram = StringField('Instagram Link')
    linkedin = StringField('Linkedin Link')
    submit = SubmitField('Save Changes')

class EditImageGalleryForm(Form):


    submit = SubmitField('Save Changes')


class EditBodyForm(Form):

    hairChoices = [('pale','Pale'),('fair','Fair'), ('light brown' , 'Light Brown') , ('dark' , 'Dark')]
    height = IntegerField('Height(in cm)')
    weight = IntegerField('Weight')
    hair_colour = StringField('Hair Colour')
    complexion = SelectField('Complexion' , choices = hairChoices)
    submit = SubmitField('Save Changes')

class DeleteProfileForm(Form):
    email = StringField('E-mail', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Confirm')
