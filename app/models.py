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
        raise AttributeError('password is not a readable attribute.')

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
    username = db.Column(db.String(60), db.ForeignKey("users.username"), nullable = False)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    image_id = db.Column(db.Integer, nullable = True)
    gender = db.Column(db.String(10), nullable = True)
    hometown = db.Column(db.String(60), nullable = True)
    dob = db.Column(db.Date, nullable = False)
    mother_tongue = db.Column(db.String(60), nullable = True)
    about = db.Column(db.String(120), nullable = True)

    def __repr(self):
        return '<Profile :{}>'.format(self.username)



@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
