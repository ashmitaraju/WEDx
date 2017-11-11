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

    maritalChoices = [('single' , 'Single') , ('divorced' , 'Divorced') , ('widow' , 'Widow/Widower') , ('poly' , 'Believe in Polygamy')]
    first_name = StringField('First Name', validators = [InputRequired()])
    last_name = StringField('Last Name', validators = [Optional()])
    gender = SelectField('Gender', choices = genderChoices)
    dob = DateField('Date of Birth', validators = [InputRequired()])
    marital_status = SelectField('Marital Status' , choices = maritalChoices , validators = [InputRequired()])
    hometown = StringField('Hometown', validators = [Optional()])
    mother_tongue = StringField('Mother Tongue', validators = [Optional()])
    about = TextField('About', validators = [Optional()])
    current_location = StringField('Current Location', validators = [Optional()])
    image = FileField('Profile Picture', validators=[myvalidator, Optional() , FileAllowed(images, 'Image only!')])
    submit = SubmitField('Save and Next')
    #nxt = SubmitField('Next')

class EditEducationForm(Form):

    school = StringField('School', validators = [Optional()])
    under_grad = StringField('Under Graduation', validators = [Optional()])
    post_grad = StringField('Post Gradution', validators = [Optional()])
    submit = SubmitField('Save and Next')
    skip = SubmitField('Skip')

class EditEmploymentForm(Form):
     occupation = StringField('Occupation', validators = [Optional()])
     designation = StringField('Designation', validators = [Optional()])
     company_name = StringField('Company Name', validators = [Optional()])
     salary = IntegerField('Salary' , validators = [Optional()])
     submit = SubmitField('Save and Next')
     skip = SubmitField('Skip')

class EditPreferencesForm(Form):
    occupation = StringField('Occupation')
    salary = IntegerField('Salary' , validators = [Optional()])
    hometown = StringField('Hometown', validators = [Optional()])
    height = IntegerField('Height (in cm)' , validators = [Optional()])
    current_location = StringField('Current Location', validators = [Optional()])
    gender = SelectField('Gender', choices = genderChoices)
    mother_tongue = StringField('Mother Tongue', validators = [Optional()])
    about = TextField('About', validators = [Optional()])
    submit = SubmitField('Save Changes')
    skip = SubmitField('Skip')

class EditSocialMediaForm(Form):

    facebook = StringField('Facebook Link', validators = [Optional()])
    twitter = StringField('Twitter Link', validators = [Optional()])
    instagram = StringField('Instagram Link', validators = [Optional()])
    linkedin = StringField('Linkedin Link', validators = [Optional()])
    submit = SubmitField('Save and Next')
    skip = SubmitField('Skip')

class EditImageGalleryForm(Form):

    image = FileField('Upload Picture(s)', validators=[myvalidator, Optional() , FileAllowed(images, 'Image only!')])
    submit = SubmitField('Save and Next')
    skip = SubmitField('Skip')

class EditBodyForm(Form):

    hairChoices = [('pale','Pale'),('fair','Fair'), ('brown' , 'Brown') , ('dark' , 'Dark')]
    height = IntegerField('Height(in cm)' , validators = [Optional()])
    weight = IntegerField('Weight' , validators = [Optional()])
    hair_colour = StringField('Hair Colour', validators = [Optional()])
    complexion = SelectField('Complexion' , choices = hairChoices)
    submit = SubmitField('Save and Next')
    skip = SubmitField('Skip')

class DeleteProfileForm(Form):
    email = StringField('E-mail', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Confirm')

class SearchFilterForm(Form):
    age = IntegerField('Age' , validators = [Optional()])
    gender = SelectField('Gender', choices = genderChoices)
    mother_tongue = StringField('Mother Tongue', validators = [Optional()])
    current_location = StringField('Current Location', validators = [Optional()])
<<<<<<< HEAD
    hometown = StringField('Hometown', validators = [Optional()])
    mother_tongue = StringField('Mother Tongue', )
    height = IntegerField('Height(in cm)' , validators = [Optional()])
    salary = IntegerField('Salary' , validators = [Optional()])
    under_grad = StringField('Under Graduation', validators = [Optional()])
    post_grad = StringField('Post Gradution', validators = [Optional()])
=======
    occupation = StringField('Occupation', validators = [Optional()])
    salary = StringField('Salary', validators = [Optional()])
    under_grad = StringField('Undergrad School', validators = [Optional()])
    post_grad = StringField('Postgrad School', validators = [Optional()])
    height = IntegerField('Height(in cm)' , validators = [Optional()])
>>>>>>> refs/remotes/origin/master
    submit = SubmitField('Search')
'''
      id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False, unique=True)
    height = db.Column(db.Integer)
    occupation = db.Column(db.String(150), nullable = True)
    salary = db.Column(db.BigInteger)
    under_grad = db.Column(db.String(150), nullable = True)
    post_grad = db.Column(db.String(150), nullable = True)
    gender = db.Column(db.String(10), nullable = True)
    hometown = db.Column(db.String(60), nullable = True)
    mother_tongue = db.Column(db.String(60), nullable = True)
    current_location = db.Column(db.String(20), nullable = True)
    dob = db.Column(db.Date, nullable = True)
'''

class SendMessageForm(Form):
    subject = StringField('Subject', validators =[DataRequired()])
    body = TextField('Body', validators = [InputRequired()])
    submit = SubmitField('Send')
