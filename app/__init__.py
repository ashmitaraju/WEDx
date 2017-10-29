from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads
import os

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')

#app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 
app.secret_key = 'red-wedding'
#images = Images(app) 

db.init_app(app)
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "login"
migrate = Migrate (app, db)
Bootstrap(app)

images = UploadSet('images', IMAGES)
configure_uploads(app, images)


from app import views, models
