from app import app
from flask import render_template, redirect, flash, url_for, request, make_response
from flask_login import login_required, login_user, logout_user, current_user
from .forms import *
from app import db, images
from .models import *
import datetime
from werkzeug.utils import secure_filename
import os
import pdfkit

def calculate_age(born):
    today = datetime.datetime.now()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

@app.route('/')
def homepage():
    return render_template('index.html', title="Welcome")

@app.route('/dashboard', methods = ['GET' , 'POST'])
@login_required
def dashboard():
    proposalForm = ProposalForm()
    quickSearchForm = QuickSearchForm()

    if proposalForm.validate_on_submit():

        username = proposalForm.toUser.data
        if ( Users.query.filter_by( username = username).first() is not None):
            body_msg = "Accept this request so that I can fill out our success story. <a href=\" /acceptProposal/" + current_user.username + "\"" + "  >Accept</a> <a href=\" /rejectProposal/" + current_user.username + "\"" + "  >Reject</a>"
            message = Messages(sender_username = current_user.username, receiver_username = proposalForm.toUser.data, subject= "Let's fill our success story.", body=body_msg , timestamp = str(datetime.datetime.now())[:16])
            db.session.add(message)
            db.session.commit() 

            print message  
            # return redirect(url_for('dashboard'))
        else:
            flash ('Invalid Username')
        # return redirect(url_for('dashboard'))
        # return redirect(url_for('dashboard'))

    elif quickSearchForm.validate_on_submit():
        text = quickSearchForm.username.data
        return redirect(url_for('viewProfile' , user = text)) 

    msgs = Messages.query.filter_by(receiver_username= current_user.username).all()
    reqs = Requests.query.filter_by(to_username = current_user.username , status = 'requested').all()
    profile = Profiles.query.filter_by(username= current_user.username).first()
    if profile is not None:
        id = profile.image_id
        image = ImageGallery.query.filter_by(imgid = id).first()
    else:
        image = None

    age = calculate_age(profile.dob)
    if profile.gender == 'male': 
        gender=1
    else:
        gender=0


    return render_template('dashboard.html', title="Dashboard", profile = profile , image = image , msgs = msgs , age = age , reqs = reqs, proposalForm = proposalForm, quickSearchForm = quickSearchForm, gender = gender) #eh wait

@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/viewProfile/<user>', methods=['GET', 'POST'])
@login_required
def viewProfile(user):
    
    allowed = Requests.query.filter_by(to_username = user , from_username = current_user.username).first()
    if user == current_user.username: 
        allowed = True

    search = Search.query.filter_by(username = user).first()
    if search.searchable == 0:
        flash('Profile does not exist')
        return redirect('dashboard')
      

    profile = Profiles.query.filter_by(username=user).first()
    pics = ImageGallery.query.filter_by(username = user).all()
    prefs = Partner_Preferences.query.filter_by(username = user).first() 
    social = Social_Media.query.filter_by(username = user).first()
    edu = Education.query.filter_by(username = user).first()
    emp = Employment.query.filter_by(username = user).first()
    bod = Body.query.filter_by(username = user).first()

    #print prefs 
    emailid = Users.query.filter_by(username = user).first()
    

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
        message = Messages(sender_username = current_user.username, receiver_username = profile.username, subject=form.subject.data, body=form.body.data , timestamp = str(datetime.datetime.now())[:16])
        db.session.add(message)
        db.session.commit()
        flash('Message sent!')
    age = calculate_age(profile.dob)
    return render_template('viewProfile.html', user = user , profile = profile, image= image,  emailid = emailid , prefs = prefs , pics = pics , form = form , age=age , allowed = allowed , social = social , edu = edu , emp = emp , bod = bod)

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
        if profile is None:
            form = EditProfileForm()
            if form.validate_on_submit():
                pic = form.image.data
                if pic is not None:
                    filename = images.save(request.files['image'])
                    url = images.url(filename)
                    image = ImageGallery(image_filename= filename, image_path= url, username= current_user.username)
                    db.session.add(image)
                    db.session.commit()
                    image = ImageGallery.query.filter_by(image_filename = filename).first()
                    profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , marital_status = form.marital_status.data , image_id = image.imgid)
                else:
                    profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , marital_status = form.marital_status.data , image_id = 18)
                db.session.add(profile)
                db.session.commit()
                age = calculate_age(profile.dob) 
                search = Search(username= current_user.username, age = age , mother_tongue= profile.mother_tongue, current_location = profile.current_location, hometown = profile.hometown, gender = profile.gender)

                db.session.add(search)
                db.session.commit()

                return redirect(url_for('editEducation'))

        else:
            form = EditProfileForm(obj=profile)
            form.populate_obj(profile)
            if form.validate_on_submit():
                pic = form.image.data
                if pic is not None:   #picture is uploaded
                    filename = images.save(request.files['image'])
                    url = images.url(filename)
                    image = ImageGallery(image_filename= filename, image_path= url, username= current_user.username)
                    db.session.add(image)
                    db.session.commit()
                    image = ImageGallery.query.filter_by(image_filename = filename).first()
                    #profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , marital_status = form.marital_status.data , image_id = image.imgid)
                    profile.image_id = image.imgid
                    db.session.commit()
                else:
                    profile = Profiles(first_name = form.first_name.data, last_name = form.last_name.data, gender = form.gender.data, dob = form.dob.data, about = form.about.data, hometown = form.hometown.data, mother_tongue = form.mother_tongue.data, username = current_user.username , current_location = form.current_location.data , marital_status = form.marital_status.data)
                    db.session.commit()
                search = Search.query.filter_by(username = current_user.username).first()
                age = calculate_age(profile.dob) 
                search.age = age
                search.mother_tongue = form.mother_tongue.data
                search.hometown = form.hometown.data
                search.current_location = form.current_location.data
                search.gender = form.gender.data
                db.session.commit()
               # print(search.current_location)

                flash('Details Updated.')
                return redirect(url_for('editEducation'))

        return render_template('editProfile.html', form = form)

@app.route('/education', methods=['GET', 'POST'])
@login_required
def editEducation():
    education = Education.query.filter_by(username = current_user.username).first()
    #search = Search.query.filter_by(username = current_user.username).first()
    if education is not None: #reediting time
        form1 = EditEducationForm(obj = education)
        form1.populate_obj(education)
        if form1.validate_on_submit():
            education = Education(school = form1.school.data , under_grad = form1.under_grad.data , post_grad = form1.post_grad.data , username = current_user.username)
            db.session.commit()
            search = Search.query.filter_by(username = current_user.username).first()
            search.under_grad = form1.under_grad.data
            search.post_grad = form1.post_grad.data
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('editEmployment'))

    else:
        form1 = EditEducationForm()
        if form1.validate_on_submit():
            education = Education(school = form1.school.data , under_grad = form1.under_grad.data , post_grad = form1.post_grad.data , username = current_user.username)
            db.session.add(education)
            db.session.commit()
            search = Search.query.filter_by(username = current_user.username).first()
            search.under_grad = form1.under_grad.data
            search.post_grad = form1.post_grad.data
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('editEmployment'))


    return render_template('education.html', form = form1)

@app.route('/employment', methods=['GET', 'POST'])
@login_required
def editEmployment():
    emp = Employment.query.filter_by(username = current_user.username).first()
   # search = Search.query.filter_by(username = current_user.username).first()
    if emp is not None:
        form2 = EditEmploymentForm(obj = emp)
        form2.populate_obj(emp)
        if form2.validate_on_submit():
            emp = Employment(occupation = form2.occupation.data , designation = form2.designation.data , company_name = form2.company_name.data , salary = form2.salary.data , username = current_user.username)
           # search = Search(occupation = form2.occupation.data , salary = form2.salary.data)
            db.session.commit()
            search = Search.query.filter_by(username = current_user.username).first()
            search.occupation = form2.occupation.data
            search.salary = form2.salary.data
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('editSocial'))
    else:
        form2 = EditEmploymentForm()
        if form2.validate_on_submit():
            emp = Employment(occupation = form2.occupation.data , designation = form2.designation.data , company_name = form2.company_name.data , salary = form2.salary.data , username = current_user.username)
            db.session.add(emp)
            db.session.commit()
            #emp = Employment.query.filter_by(username = current_user.username).first()
            #search = Search(occupation = form2.occupation.data , salary = form2.salary.data)
            search = Search.query.filter_by(username = current_user.username).first()
            search.occupation = form2.occupation.data
            search.salary = form2.salary.data
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('editSocial'))


    return render_template('employment.html', form = form2)

@app.route('/social', methods=['GET', 'POST'])
@login_required
def editSocial():
    soc = Social_Media.query.filter_by(username = current_user.username).first()
    if soc is not None:
        form3 = EditSocialMediaForm(obj = soc)
        form3.populate_obj(soc)
        if form3.validate_on_submit():
            soc = Social_Media(facebook = form3.facebook.data , twitter = form3.twitter.data , instagram = form3.instagram.data , linkedin = form3.linkedin.data , username = current_user.username)
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('editImages'))
    else:
        form3=EditSocialMediaForm()
        if form3.validate_on_submit():
            soc = Social_Media(facebook = form3.facebook.data , twitter = form3.twitter.data , instagram = form3.instagram.data , linkedin = form3.linkedin.data , username = current_user.username)
            db.session.add(soc)
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('editImages'))

    return render_template('social.html', form = form3)

@app.route('/uploadImages', methods=['GET', 'POST'])
@login_required
def editImages():

    pics = ImageGallery.query.filter_by(username = current_user.username).all() 
    print pics 

    form4 = EditImageGalleryForm()

    if form4.skip.data:
        return redirect(url_for('editBody'))

    if form4.submit.data: 
        if 'image' in request.files:
            for f in request.files.getlist('image'):
                if f.filename:
                    print "hey"
                    print f.filename 
                    filename = secure_filename(f.filename)
                    f.save(os.path.join(app.config['UPLOADED_IMAGES_DEST'], filename))
                    url = "../static/img/" + filename
                    image = ImageGallery(image_filename= filename, image_path= url, username= current_user.username)
                    db.session.add(image)
                    db.session.commit()
            return redirect(url_for('editBody'))
        else:
            print "hey"
            return redirect(url_for('editBody'))

    return render_template('image.html' , form = form4 , pics = pics)

@app.route('/body', methods=['GET', 'POST'])
@login_required
def editBody():
    bod = Body.query.filter_by(username = current_user.username).first()
    search = Search.query.filter_by(username = current_user.username).first()
    if bod is not None:
        form5 = EditBodyForm(obj = bod)
        form5.populate_obj(bod)
        if form5.validate_on_submit():
            bod = Body(height = form5.height.data , weight = form5.weight.data , complexion = form5.complexion.data , hair_colour = form5.hair_colour.data , username = current_user.username)
            search = Search.query.filter_by(username = current_user.username).first()
            search.height = form5.height.data
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('editPreferences'))
    else:
        form5 = EditBodyForm()
        if form5.validate_on_submit():
            bod = Body(height = form5.height.data , weight = form5.weight.data , complexion = form5.complexion.data , hair_colour = form5.hair_colour.data , username = current_user.username)
            db.session.add(bod)
            db.session.commit()
            bod = Body.query.filter_by(username = current_user.username).first()
            search = Search.query.filter_by(username = current_user.username).first()
            search.height = form5.height.data
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('editPreferences'))

    return render_template('body.html', form = form5)

@app.route('/preferences', methods=['GET', 'POST'])
@login_required
def editPreferences():
    pref = Partner_Preferences.query.filter_by(username = current_user.username).first()
    if pref is not None:
        form6 = EditPreferencesForm(obj = pref)
        form6.populate_obj(pref)
        if form6.validate_on_submit():
            pref = Partner_Preferences(height = form6.height.data , occupation = form6.occupation.data , salary = form6.salary.data , gender = form6.gender.data , hometown = form6.hometown.data , mother_tongue = form6.mother_tongue.data , current_location = form6.current_location.data , about = form6.about.data , username = current_user.username)
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('dashboard'))
    else:
        form6=EditPreferencesForm()
        if form6.validate_on_submit():
            pref = Partner_Preferences(height = form6.height.data , occupation = form6.occupation.data , salary = form6.salary.data , gender = form6.gender.data , hometown = form6.hometown.data , mother_tongue = form6.mother_tongue.data , current_location = form6.current_location.data , about = form6.about.data , username = current_user.username)
            db.session.add(pref)
            db.session.commit()
            flash('Details Updated.')
            return redirect(url_for('dashboard'))

    return render_template('preferences.html', form = form6)

@app.route('/advancedSearch', methods=['GET', 'POST'])
@login_required
def advancedSearch():
    form = SearchFilterForm()
    if form.validate_on_submit():
        search = {}
        if form.age_lower.data:
            age_lower = form.age_lower.data
        else:
            age_lower = 18 

        if form.age_upper.data:
            age_upper = form.age_upper.data 
        else:
            age_upper = 100

        for field in form:
            if (field.data and field.name != 'csrf_token' and field.name != 'submit' and field.name != 'age_lower' and field.name != 'age_upper'):
                search.update({field.name : field.data})
        
        results = Search.query.filter_by(**search)
        results_list = list(results)

        if results is not None:
            for res in results_list: 
                if res.age <= age_lower or res.age >= age_upper or res.searchable == 0:
                    results_list.remove(res)  
        else: 
            results = Search.query.filter_by(age >= age_lower , age <=age_upper) 
        
        results = results_list 

        #images = [] 
        profiles = []
        for user in results:
            if user.username != current_user.username:
                profile = Profiles.query.filter_by(username = user.username).first()  
                image = ImageGallery.query.filter_by(imgid = profile.image_id).first()
                social = Social_Media.query.filter_by(username = profile.username).first()
                if image is None and social is None: 
                    profiles.append([profile , False , False]) 
                elif image is None and social is not None: 
                    profiles.append([profile , False , social ])
                elif image is not None and social is None: 
                    profiles.append([profile , image , False])
                else: 
                    profiles.append([profile , image , social])
        
        print profiles

        return render_template('searchResults.html', profiles = profiles , images = images)

    return render_template('advancedSearch.html', form = form)

@app.route('/replyMessage/<mid>', methods=['GET', 'POST'])
@login_required
def replyMessage(mid):
    form = SendMessageForm()
    message = Messages.query.filter_by(msgid= mid).first()
   # print message.sender_username
    
    if form.validate_on_submit():
        newMessage = Messages(sender_username = current_user.username, receiver_username = message.sender_username, subject = form.subject.data, body = form.body.data, timestamp = str(datetime.datetime.now())[:16])
        db.session.add(newMessage)
        db.session.commit()
        flash('Message Sent!')
        return redirect(url_for('dashboard'))

    return render_template('replyMessage.html', form = form, message = message)

@app.route('/deleteMessage/<mid>', methods=['GET', 'POST'])
@login_required
def deleteMessage(mid):
    message = Messages.query.filter_by(msgid= mid).first()
    
    db.session.delete(message)
    db.session.commit()
    flash('Message Deleted')
    return redirect(url_for('dashboard'))

@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = DeleteProfileForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
                if current_user.email == form.email.data:
                    return redirect('/deactivateconfirm') 
                else:
                    flash('Invalid Email ID. Please enter again.')
                    return redirect('delete')

    return render_template('delete.html', title= 'Delete Profile', form=form)

@app.route('/deleteconfirm', methods=['GET', 'POST'])
@login_required
def deleteconfirm():
        return render_template('delete-confirm.html')

@app.route("/forward/", methods=['POST', 'GET'])
@login_required
def move_forward():
    user = current_user
    images = ImageGallery.query.filter_by(username= current_user.username).all()
    for image in images:
         os.remove(os.path.join(app.config['UPLOADED_IMAGES_DEST'], image.image_filename))
    
    db.session.delete(user)
    db.session.commit()

    flash('Ciao')
    return redirect('logout')

@app.route('/deactivateconfirm', methods=['GET', 'POST'])
@login_required
def deactivate_confirm():
    return render_template('deactivate.html')

@app.route('/deactivate', methods=['GET', 'POST'])
@login_required
def deactivate():
    user = current_user
    search = Search.query.filter_by(username = user.username).first()
    search.searchable = 0 
    flash('Account has been deactivated.')
    db.session.commit()
    return redirect('logout') 

@app.route('/activate', methods=['GET', 'POST'])
@login_required
def activate():
    user = current_user
    search = Search.query.filter_by(username = user.username).first()
    search.searchable = 1 
    flash('Account has been activated.')
    db.session.commit()
    return redirect('dashboard') 


@app.route("/request/<toUser>", methods=['POST', 'GET'])
@login_required
def requested(toUser): 
    request = Requests(from_username = current_user.username , to_username = toUser , status = 'requested')
    db.session.add(request)
    db.session.commit() 
    flash (' Request Sent')
    return redirect(url_for('dashboard')) 

@app.route("/acceptRequest/<rid>", methods=['POST', 'GET'])
@login_required
def acceptRequest(rid): 
    req = Requests.query.filter_by(request_id = rid).first()
    #req = Requests(from_username = current_user.username , to_username = req.to_username , status = 'accepted')
    req.status='accepted'
    body_msg = current_user.username + " has accepted your request to view their profile."
    message = Messages(sender_username = current_user.username, receiver_username = req.from_username, subject= "Request Accepted", body=body_msg , timestamp = str(datetime.datetime.now())[:16])
    db.session.add(message)
    db.session.commit()
    return redirect(url_for('dashboard'))   


@app.route("/rejectRequest/<rid>", methods=['POST', 'GET'])
@login_required
def rejectRequest(rid): 
    req = Requests.query.filter_by(request_id = rid).first()
    #req = Requests(from_username = current_user.username , to_username = toUser , status = 'rejected')
    req.status='rejected'
    body_msg = current_user.username + " has accepted your request to view their profile."
    message = Messages(sender_username = current_user.username, receiver_username = req.from_username, subject= "Request Rejected", body=body_msg , timestamp = str(datetime.datetime.now())[:16])
    db.session.commit() 
    return redirect(url_for('dashboard')) 


@app.route("/createStory/<user2>", methods=['POST', 'GET'])
@login_required
def createStory(user2): 
    
    form = CreateStoryForm()

    if form.validate_on_submit():
        story = successStories(username1= current_user.username, username2 = user2, story = form.story.data, timestamp = str(datetime.datetime.now()) [:16])
        db.session.add(story)
        db.session.commit()
        return redirect (url_for('dashboard'))
             
    return render_template('createStory.html', form = form) 


@app.route("/acceptProposal/<user2>", methods=['POST', 'GET'])
@login_required
def acceptProposal(user2): 

    body_msg = current_user.username + " has accepted your request to fill stories. Please deactivate your profile so that it is not searchable and not viewable.   <a href=\" /createStory/" + current_user.username + "\"" + "  >Please add story.</a>"
    message = Messages(sender_username = current_user.username, receiver_username = user2, subject= "Request to fill story Accepted", body=body_msg , timestamp = str(datetime.datetime.now())[:16])
    db.session.add(message)
    print "hi"
    db.session.commit()
    user = current_user
    search = Search.query.filter_by(username = user.username).first()
    search.searchable = 'False'
    user = user2 
    search = Search.query.filter_by(username = user2).first()
    search.searchable = 'False'
    db.session.commit()
    return redirect(url_for('dashboard'))


@app.route("/rejectProposal/<user2>", methods=['POST', 'GET'])
@login_required
def rejectProposal(user2): 

    body_msg = current_user.username + " has rejected your request to fill a story. "
    message = Messages(sender_username = current_user.username, receiver_username = user2, subject= "Request to fill story Rejected", body=body_msg , timestamp = str(datetime.datetime.now())[:16])
    db.session.add(message)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route("/viewStories", methods=['POST', 'GET'])
def viewStories(): 

    stories = successStories.query.all()
    story_dict=[]

    for story in stories:
        profile1 = Profiles.query.filter_by(username = story.username1).first()
        search1 = Search.query.filter_by(username = story.username1).first()

        profile2 = Profiles.query.filter_by(username = story.username2).first()
        search2 = Search.query.filter_by(username = story.username2).first()

        print story.username1 
        print story.username2

        if search1.searchable == 0 or search2.searchable == 0:
            print "hey"
            break

        image1 = ImageGallery.query.filter_by(imgid = profile1.image_id).first()
        image2 = ImageGallery.query.filter_by(imgid = profile2.image_id).first()
        print "hi"
           
        cur_list = [profile1.first_name , profile1.last_name , profile2.first_name , profile2.last_name , image1.image_path , image2.image_path , story.story ]
        story_dict.append(cur_list) 

    return render_template('viewStories.html', stories = story_dict) 

@app.route('/generateBio')
@login_required
def generateBio():
    profile = Profiles.query.filter_by(username=current_user.username).first()
    pics = ImageGallery.query.filter_by(username = current_user.username).all()
    prefs = Partner_Preferences.query.filter_by(username = current_user.username).first() 
    social = Social_Media.query.filter_by(username = current_user.username).first()
    edu = Education.query.filter_by(username = current_user.username).first()
    emp = Employment.query.filter_by(username = current_user.username).first()
    bod = Body.query.filter_by(username = current_user.username).first()
    #print prefs 
    emailid = Users.query.filter_by(username = current_user.username).first()
    

    if profile is None:
        flash('Profile does not exist')
        return redirect('dashboard')
    else:
        id = profile.image_id
        image = ImageGallery.query.filter_by(imgid = id).first()


    gender = {'male' : False}
    if (str(profile.gender) == "male"):
        gender['male'] = True

    age = calculate_age(profile.dob)

    rendered = render_template('generateBio.html', profile = profile, image= image,  emailid = emailid , prefs = prefs , pics = pics , age=age , social=social , edu=edu,emp=emp,bod=bod)
  
    pdf = pdfkit.from_string(rendered, False,)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response




    

#did you create a story? mean husband 
#if conditions haak beku 
#haku
#or we'll put a default img_path for all profiless. yes we will .
#imgid numbering starts with 0 or 1?
#1 
#okay so we'll insert the dummy as zero and make all the profiles with no dps point at that?
#S. you never fail to make me kringe
#clearing traces
#where do we insert that dummy image 
#i did that. i'm talking about inserting into db
#lets just write one line to insert it now and then remove the line 
#but there has to be someway of keeping static stuff in the db no
#bby call madi
 