from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Users(UserMixin, db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Profiles(UserMixin, db.Model):
    __tablename__ = 'Profiles'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    image_id = db.Column(db.Integer, nullable = True)
    gender = db.Column(db.String(10), nullable = True)
    hometown = db.Column(db.String(60), nullable = True)
    dob = db.Column(db.Date, nullable = False)
    mother_tongue = db.Column(db.String(60), nullable = True)
    about = db.Column(db.Text, nullable = True)
    marital_status = db.Column(db.String(20), nullable = True)
    current_location = db.Column(db.String(20), nullable = True)
    def __repr(self):
        return '<Profile :{}>'.format(self.username)

class Social_Media(UserMixin, db.Model):
    __tablename__= 'Social_Media'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False)
    facebook = db.Column(db.String(150), nullable = True)
    instagram = db.Column(db.String(150), nullable = True)
    linkedin = db.Column(db.String(150), nullable = True)
    twitter = db.Column(db.String(150), nullable = True)
    def __repr(self):
        return '<Social_Media :{}>'.format(self.username)

class Education(UserMixin, db.Model):
    __tablename__= 'Education'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False)
    school = db.Column(db.String(150), nullable = False)
    under_grad = db.Column(db.String(150), nullable = True)
    post_grad = db.Column(db.String(150), nullable = True)
    def __repr(self):
        return '<Education :{}>'.format(self.username)

class Employment(UserMixin, db.Model):
    __tablename__= 'Employment'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False)
    occupation = db.Column(db.String(150), nullable = True)
    designation = db.Column(db.String(150), nullable = True)
    company_name = db.Column(db.String(150), nullable = True)
    salary = db.Column(db.BigInteger, nullable = True)
    def __repr(self):
        return '<Employment :{}>'.format(self.username)

class Body(UserMixin, db.Model):
    __tablename__= 'Body'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False)
    height = db.Column(db.Integer, nullable = True)
    weight =  db.Column(db.Integer, nullable = True)
    complexion = db.Column(db.String(10), nullable = True)
    hair_colour = db.Column(db.String(10), nullable = True)

    def __repr(self):
        return '<Body :{}>'.format(self.username)

class Partner_Preferences(UserMixin, db.Model):
    __tablename__= 'Partner_Preferences'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False)
    height = db.Column(db.Integer, nullable = True)
    occupation = db.Column(db.String(150), nullable = True)
    salary = db.Column(db.BigInteger, nullable = True)
    gender = db.Column(db.String(10), nullable = True)
    hometown = db.Column(db.String(60), nullable = True)
    mother_tongue = db.Column(db.String(60), nullable = True)
    current_location = db.Column(db.String(20), nullable = True)
    about = db.Column(db.Text, nullable = True)
    def __repr(self):
        return '<Partner_Preferences :{}>'.format(self.username)

class ImageGallery(UserMixin, db.Model):
    __tablename__= 'ImageGallery'

    imgid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False)
    image_filename = db.Column(db.String(60), default= None, nullable= False)
    image_path = db.Column(db.Text, default= None, nullable = False)


    def __repr(self):
        return '<ImageGallery :{}>'.format(self.username)

class Search(UserMixin, db.Model):
    __tablename__= 'Search'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), db.ForeignKey("users.username", ondelete='CASCADE'), nullable = False)
    height = db.Column(db.Integer, nullable = True)
    occupation = db.Column(db.String(150), nullable = True)
    salary = db.Column(db.BigInteger, nullable = True)
    under_grad = db.Column(db.String(150), nullable = True)
    post_grad = db.Column(db.String(150), nullable = True)
    gender = db.Column(db.String(10), nullable = True)
    hometown = db.Column(db.String(60), nullable = True)
    mother_tongue = db.Column(db.String(60), nullable = True)
    current_location = db.Column(db.String(20), nullable = True)
    dob = db.Column(db.Date, nullable = True)

    def __repr(self):
        return '<Search :{}>'.format(self.username)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
