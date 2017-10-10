from flask import Flask

app = Flask(__name__)
#from app import views

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
