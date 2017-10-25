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
    messages = Messages.query.filter_by(receiver_username= current_user.username).all()
    profile = Profiles.query.filter_by(username= current_user.username).first()
    if profile is not None:
        id = profile.image_id
        image = ImageGallery.query.filter_by(imgid = id).first()
    else:
        image = None
    return render_template('dashboard.html', title="Dashboard", profile = profile , image = image , messages = messages)


@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')



@app.route('/viewProfile/<user>', methods=['GET', 'POST'])
@login_required
def viewProfile(user):

    profile = Profiles.query.filter_by(username=user).first()
    if profile is None:
        flash('Profile does not exist')
        return redirect('dashboard')
    else:
        id = profile.image_id
        image = ImageGallery.query.filter_by(imgid = id).first()


    gender = {'male' : False}
    if (str(profile.gender) == "male"):
        gender['male'] = True

    form = SendMessageForm()
    if form.validate_on_submit():
        message = Messages(sender_username = current_user.username, receiver_username = profile.username, subject=form.subject.data, body=form.subject.data)
        db.session.add(message)
        db.session.commit()
        flash('Message sent!')
    return render_template('viewProfile.html', title = profile.first_name, profile = profile, gender = gender, image= image, form = form)




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
        profile = Profiles.query.filter_by(username = current_user.username).first()
        search = Search.query.filter_by(username = current_user.username).first()
        """
        education = Education.query.filter_by(username = current_user.username).first()
        emp = Employment.query.filter_by(username = current_user.username).first()
        soc = Social_Media.query.filter_by(username = current_user.username).first()
        bod = Body.query.filter_by(username = current_user.username).first()
        pref = Partner_Preferences.query.filter_by(username = current_user.username).first()
        """
        if profile is None:
            form = EditProfileForm()
            """
            form1 = EditEducationForm()
            form2 = EditEmploymentForm()
            form3 = EditSocialMediaForm()
            form4 = EditImageGalleryForm()
            form5 = EditBodyForm()
            form6 = EditPreferencesForm()
            """
            if form.validate_on_submit():
                pic = form.image.data
                if pic is not None:
                    filename = images.save(request.files['image'])
                    url = images.url(filename)
                    image = ImageGallery(image_filename= filename, image_path= url, username= current_user.username)
                    #profile.image_id = image.imgid
                    db.session.add(image)
                    db.session.commit()
                    image = ImageGallery.query.filter_by(image_filename = filename).first()
                    profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , marital_status = form.marital_status.data , image_id = image.imgid)
                else:
                    profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , marital_status = form.marital_status.data)
                db.session.add(profile)
                db.session.commit()
                search = Search(username= current_user.username, dob = profile.dob, mother_tongue= profile.mother_tongue, current_location = profile.current_location, hometown = profile.hometown, gender = profile.gender)

                db.session.add(search)
                db.session.commit()

                return redirect(url_for('editProfile', title= 'Edit Profile', form = form , form1=form1 , form2=form2 , form3=form3 , form4=form4 , form5=form5 , form6=form6))

        else :
            form = EditProfileForm(obj=profile)
            form.populate_obj(profile)

            form.populate_obj(profile)
            """
            if education is not None:
                form1 = EditEducationForm(obj = education)
                form1.populate_obj(education)
            else:
                form1 = EditEducationForm()

            if emp is not None:
                form2 = EditEmploymentForm(obj = emp)
                form2.populate_obj(emp)
            else:
                form2 = EditEmploymentForm()

            if soc is not None:
                form3 = EditSocialMediaForm(obj = soc)
                form3.populate_obj(soc)
            else:
                form3=EditSocialMediaForm()

            if bod is not None:
                form5 = EditBodyForm(obj = bod)
                form5.populate_obj(bod)
            else:
                form5 = EditBodyForm()

            if pref is not None:
                form6 = EditPreferencesForm(obj = pref)
                form6.populate_obj(pref)
            else:
                form6=EditPreferencesForm()
            """
            if form.validate_on_submit():
                pic = form.image.data
                if pic is not None:   #picture is uploaded
                    filename = images.save(request.files['image'])
                    url = images.url(filename)
                    image = ImageGallery(image_filename= filename, image_path= url, username= current_user.username)
                    db.session.add(image)
                    db.session.commit()
                    image = ImageGallery.query.filter_by(image_filename = filename).first()
                    profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , marital_status = form.marital_status.data , image_id = image.imgid)
                else:
                    profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , marital_status = form.marital_status.data)

                search = Search(username= current_user.username, dob = profile.dob, mother_tongue= profile.mother_tongue, current_location = profile.current_location, hometown = profile.hometown, gender = profile.gender)
                db.session.commit()

                flash('Details Updated.')


            return render_template('education.html', title= 'Edit Profile', form = form )
"""
@app.route('/education', methods=['GET', 'POST'])
@login_required
def editEducation():

@app.route('/employment', methods=['GET', 'POST'])
@login_required
def editEmployment():

@app.route('/social', methods=['GET', 'POST'])
@login_required
def editSocial():

@app.route('/body', methods=['GET', 'POST'])
@login_required
def editBody():

@app.route('/preferences', methods=['GET', 'POST'])
@login_required
def editPreferences():
"""

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
