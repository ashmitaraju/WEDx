from app import app
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from .forms import *
from app import db, images
from .models import *


@app.route('/')
def homepage():
    return render_template('index.html', title="Welcome")


@app.route('/dashboard')
@login_required
def dashboard():
    profile = Profiles.query.filter_by(username= current_user.username).first()

    return render_template('dashboard.html', title="Dashboard", profile = profile)


@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')



@app.route('/viewProfile/<user>', methods=['GET', 'POST'])
@login_required
def viewProfile(user):

    profile = Profiles.query.filter_by(username=user).first()
    image = ImageGallery.query.filter_by(username=user).first()
    if profile is None:
        flash('Profile does not exist')
        return redirect('dashboard')

    gender = {'male' : False}
    if (str(profile.gender) == "male"):
        gender['male'] = True
    return render_template('viewProfile.html', title = profile.first_name, profile = profile, gender = gender, image= image)




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
        user = Users(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Registration Successful! You may now create your profile.')
        return redirect(url_for('editProfile'))
    return render_template('signup.html', title='Sign Up', form = form)





@app.route('/editProfile', methods=['GET', 'POST'])
@login_required
def editProfile():
    profile = Profiles.query.filter_by(username=current_user.username).first()
    search = Search.query.filter_by(username = current_user.username).first()


    if profile is None:
        form = EditProfileForm()
        form1=EditEducationForm()
        form2=EditEmploymentForm()
        form3=EditSocialMediaForm()
        form4=EditImageGalleryForm()
        form5=EditBodyForm()
        form6=EditPreferencesForm()

        if form.validate_on_submit():
            filename = images.save(request.files['image'])
            url = images.url(filename)
            image = ImageGallery(image_filename= filename, image_path= url, username= current_user.username)
            profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , image_id = image.imgid)
            search = Search(username= current_user.username, dob = profile.dob, mother_tongue= profile.mother_tongue, current_location = profile.current_location, hometown = profile.hometown, gender = profile.gender)
            db.session.add(image)
            db.session.add(profile)

            db.session.add(search)
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('dashboard'))

        if form.validate_on_submit():
            #education = Education()
            db.session.add(profile)
            db.session.add(image)
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('dashboard'))


    else :
        form = EditProfileForm(obj=profile)

        form1=EditEducationForm()
        form2=EditEmploymentForm()
        form3=EditSocialMediaForm()
        form4=EditImageGalleryForm()
        form5=EditBodyForm()
        form6=EditPreferencesForm()

        form.populate_obj(profile)
        if form.validate_on_submit():
            filename = images.save(request.files['image'])
            url = images.url(filename)
            image = ImageGallery(image_filename= filename, image_path= url, username= current_user.username)
            search = Search(username= current_user.username, dob = profile.dob, mother_tongue= profile.mother_tongue, current_location = profile.current_location, hometown = profile.hometown, gender = profile.gender)

            db.session.add(image)
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('dashboard'))



    return render_template('editProfile.html', title= 'Edit Profile', form = form , form1=form1 , form2=form2 , form3=form3 , form4=form4 , form5=form5 , form6=form6)


@app.route('/advancedSearch', methods=['GET', 'POST'])
@login_required
def advancedSearch():
    form = SearchFilterForm()
    return render_template('advancedSearch.html', form = form)

@app.route('/searchResults', methods=['GET', 'POST'])
@login_required
def searchResults():

    #search = Search.query.filter_by(username = current_user.username)
    return render_template('searchResults.html')

@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = DeleteProfileForm(request.form)
    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
                if current_user.email == form.email.data:
                    return redirect('deleteconfirm') #review
                else:
                    flash('Invalid Email ID. Please enter again.')
                    return redirect('delete')
    else:
        flash('Invlaid email or password')

    return render_template('delete.html', title= 'Delete Profile', form=form)

@app.route('/deleteconfirm', methods=['GET', 'POST'])
@login_required
def deleteconfirm():
        return render_template('delete-confirm.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    user = current_user
    db.session.delete(user)
    db.session.commit()
    flash('Ciao')
    return redirect('logout')
