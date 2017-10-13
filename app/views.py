from app import app
from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user
from .forms import LoginForm, SignUpForm
from app import db
from .models import Users

@app.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('index.html', title="Welcome")

@app.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('dashboard.html', title="Dashboard")

@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect('dashboard') #review

        else:
            flash('Invlaid email or password')

    return render_template('login.html', title='Sign In', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out.')

    return redirect(url_for('login'))

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = Users(email=form.email.data, username=form.username.data, password=form.password.data, first_name=form.first_name.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful! You may now login.')
        return redirect(url_for('login'))




    return render_template('signup.html', title='Sign Up', form = form)
