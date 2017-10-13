from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap



db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "login"
migrate = Migrate (app, db)
Bootstrap(app)








from app import views, models
