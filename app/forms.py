from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField,  TextField, ValidationError , IntegerField
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo, Required , Optional, StopValidation
from wtforms.fields.html5 import DateField

from .models import *

from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images

def myvalidator(form, field):

    if not form.image.data:

        field.errors[:] = []
        raise StopValidation()



genderChoices = [('male', 'Male'),('female', 'Female')]

class LoginForm(Form):
    email = StringField('E-mail', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(Form):
    email = StringField('E-Mail', validators = [InputRequired(), Email()])
    username = StringField('Username', validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use')

    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use')


class EditProfileForm(Form):

    genderChoices = [('male', 'Male'),('female', 'Female')]

    maritalChoices = [('single' , 'Single') , ('divorced' , 'Divorced') , ('widow' , 'Widow/Widower') , ('poly' , 'Believe in Polygamy')]

    first_name = StringField('First Name', validators = [InputRequired()])
    last_name = StringField('Last Name')
    gender = SelectField('Gender', choices = genderChoices)
    dob = DateField('Date of Birth', validators = [InputRequired()])
    marital_status = SelectField('Marital Status' , choices = maritalChoices , validators = [InputRequired()])
    hometown = StringField('Hometown')
    mother_tongue = StringField('Mother Tongue')
    about = TextField('About')
    current_location = StringField('Current Location')
    image = FileField('Profile Picture', validators=[myvalidator, Optional()])
    submit = SubmitField('Save Changes')



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

class SearchFilterForm(Form):
    gender = SelectField('Gender', choices = genderChoices)
    mother_tongue = StringField('Mother Tongue')
    current_location = StringField('Current Location')
    hometown = StringField('Hometown')
    submit = SubmitField('Search')
