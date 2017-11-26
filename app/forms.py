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
langs = [('','Select Language'),('Hindi','Hindi'),('Bengali','Bengali'),('Telugu','Telugu'),('Marathi','Marathi'),('Tamil','Tamil'),('Urdu','Urdu'),('Kannada','Kannada'),('Gujarati','Gujarati'),('Odia','Odia'),('Malayalam','Malayalam'),('English','English'),('Sanskrit','Sanskrit')]
cities = [('','Select Location'),('Adilabad','Adilabad'),('Agra','Agra'),('Ahmedabad','Ahmedabad'),('Ahmednagar','Ahmednagar'),('Aizawl','Aizawl'),('Ajitgarh (Mohali)','Ajitgarh (Mohali)'),('Ajmer','Ajmer'),('Akola','Akola'),('Alappuzha','Alappuzha'),('Aligarh','Aligarh'),('Alirajpur','Alirajpur'),('Allahabad','Allahabad'),('Almora','Almora'),('Alwar','Alwar'),('Ambala','Ambala'),('Ambedkar Nagar','Ambedkar Nagar'),('Amravati','Amravati'),('Amreli district','Amreli district'),('Amritsar','Amritsar'),('Anand','Anand'),('Anantapur','Anantapur'),('Anantnag','Anantnag'),('Angul','Angul'),('Anjaw','Anjaw'),('Anuppur','Anuppur'),('Araria','Araria'),('Ariyalur','Ariyalur'),('Arwal','Arwal'),('Ashok Nagar','Ashok Nagar'),('Auraiya','Auraiya'),('Aurangabad','Aurangabad'),('Aurangabad','Aurangabad'),('Azamgarh','Azamgarh'),('Badgam','Badgam'),('Bagalkot','Bagalkot'),('Bageshwar','Bageshwar'),('Bagpat','Bagpat'),('Bahraich','Bahraich'),('Baksa','Baksa'),('Balaghat','Balaghat'),('Balangir','Balangir'),('Balasore','Balasore'),('Ballia','Ballia'),('Balrampur','Balrampur'),('Banaskantha','Banaskantha'),('Banda','Banda'),('Bandipora','Bandipora'),('Bangalore Rural','Bangalore Rural'),('Bangalore Urban','Bangalore Urban'),('Banka','Banka'),('Bankura','Bankura'),('Banswara','Banswara'),('Barabanki','Barabanki'),('Baramulla','Baramulla'),('Baran','Baran'),('Bardhaman','Bardhaman'),('Bareilly','Bareilly'),('Bargarh (Baragarh)','Bargarh (Baragarh)'),('Barmer','Barmer'),('Barnala','Barnala'),('Barpeta','Barpeta'),('Barwani','Barwani'),('Bastar','Bastar'),('Basti','Basti'),('Bathinda','Bathinda'),('Beed','Beed'),('Begusarai','Begusarai'),('Belgaum','Belgaum'),('Bellary','Bellary'),('Betul','Betul'),('Bhadrak','Bhadrak'),('Bhagalpur','Bhagalpur'),('Bhandara','Bhandara'),('Bharatpur','Bharatpur'),('Bharuch','Bharuch'),('Bhavnagar','Bhavnagar'),('Bhilwara','Bhilwara'),('Bhind','Bhind'),('Bhiwani','Bhiwani'),('Bhojpur','Bhojpur'),('Bhopal','Bhopal'),('Bidar','Bidar'),('Bijapur','Bijapur'),('Bijapur','Bijapur'),('Bijnor','Bijnor'),('Bikaner','Bikaner'),('Bilaspur','Bilaspur'),('Bilaspur','Bilaspur'),('Birbhum','Birbhum'),('Bishnupur','Bishnupur'),('Bokaro','Bokaro'),('Bongaigaon','Bongaigaon'),('Boudh (Bauda)','Boudh (Bauda)'),('Budaun','Budaun'),('Bulandshahr','Bulandshahr'),('Buldhana','Buldhana'),('Bundi','Bundi'),('Burhanpur','Burhanpur'),('Buxar','Buxar'),('Cachar','Cachar'),('Central Delhi','Central Delhi'),('Chamarajnagar','Chamarajnagar'),('Chamba','Chamba'),('Chamoli','Chamoli'),('Champawat','Champawat'),('Champhai','Champhai'),('Chandauli','Chandauli'),('Chandel','Chandel'),('Chandigarh','Chandigarh'),('Chandrapur','Chandrapur'),('Changlang','Changlang'),('Chatra','Chatra'),('Chennai','Chennai'),('Chhatarpur','Chhatarpur'),('Chhatrapati Shahuji Maharaj Nagar','Chhatrapati Shahuji Maharaj Nagar'),('Chhindwara','Chhindwara'),('Chikkaballapur','Chikkaballapur'),('Chikkamagaluru','Chikkamagaluru'),('Chirang','Chirang'),('Chitradurga','Chitradurga'),('Chitrakoot','Chitrakoot'),('Chittoor','Chittoor'),('Chittorgarh','Chittorgarh'),('Churachandpur','Churachandpur'),('Churu','Churu'),('Coimbatore','Coimbatore'),('Cooch Behar','Cooch Behar'),('Cuddalore','Cuddalore'),('Cuttack','Cuttack'),('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),('Dahod','Dahod'),('Dakshin Dinajpur','Dakshin Dinajpur'),('Dakshina Kannada','Dakshina Kannada'),('Daman','Daman'),('Damoh','Damoh'),('Dantewada','Dantewada'),('Darbhanga','Darbhanga'),('Darjeeling','Darjeeling'),('Darrang','Darrang'),('Datia','Datia'),('Dausa','Dausa'),('Davanagere','Davanagere'),('Debagarh (Deogarh)','Debagarh (Deogarh)'),('Dehradun','Dehradun'),('Deoghar','Deoghar'),('Deoria','Deoria'),('Dewas','Dewas'),('Dhalai','Dhalai'),('Dhamtari','Dhamtari'),('Dhanbad','Dhanbad'),('Dhar','Dhar'),('Dharmapuri','Dharmapuri'),('Dharwad','Dharwad'),('Dhemaji','Dhemaji'),('Dhenkanal','Dhenkanal'),('Dholpur','Dholpur'),('Dhubri','Dhubri'),('Dhule','Dhule'),('Dibang Valley','Dibang Valley'),('Dibrugarh','Dibrugarh'),('Dima Hasao','Dima Hasao'),('Dimapur','Dimapur'),('Dindigul','Dindigul'),('Dindori','Dindori'),('Diu','Diu'),('Doda','Doda'),('Dumka','Dumka'),('Dungapur','Dungapur'),('Durg','Durg'),('East Champaran','East Champaran'),('East Delhi','East Delhi'),('East Garo Hills','East Garo Hills'),('East Khasi Hills','East Khasi Hills'),('East Siang','East Siang'),('East Sikkim','East Sikkim'),('East Singhbhum','East Singhbhum'),('Eluru','Eluru'),('Ernakulam','Ernakulam'),('Erode','Erode'),('Etah','Etah'),('Etawah','Etawah'),('Faizabad','Faizabad'),('Faridabad','Faridabad'),('Faridkot','Faridkot'),('Farrukhabad','Farrukhabad'),('Fatehabad','Fatehabad'),('Fatehgarh Sahib','Fatehgarh Sahib'),('Fatehpur','Fatehpur'),('Fazilka','Fazilka'),('Firozabad','Firozabad'),('Firozpur','Firozpur'),('Gadag','Gadag'),('Gadchiroli','Gadchiroli'),('Gajapati','Gajapati'),('Ganderbal','Ganderbal'),('Gandhinagar','Gandhinagar'),('Ganganagar','Ganganagar'),('Ganjam','Ganjam'),('Garhwa','Garhwa'),('Gautam Buddh Nagar','Gautam Buddh Nagar'),('Gaya','Gaya'),('Ghaziabad','Ghaziabad'),('Ghazipur','Ghazipur'),('Giridih','Giridih'),('Goalpara','Goalpara'),('Godda','Godda'),('Golaghat','Golaghat'),('Gonda','Gonda'),('Gondia','Gondia'),('Gopalganj','Gopalganj'),('Gorakhpur','Gorakhpur'),('Gulbarga','Gulbarga'),('Gumla','Gumla'),('Guna','Guna'),('Guntur','Guntur'),('Gurdaspur','Gurdaspur'),('Gurgaon','Gurgaon'),('Gwalior','Gwalior'),('Hailakandi','Hailakandi'),('Hamirpur','Hamirpur'),('Hamirpur','Hamirpur'),('Hanumangarh','Hanumangarh'),('Harda','Harda'),('Hardoi','Hardoi'),('Haridwar','Haridwar'),('Hassan','Hassan'),('Haveri district','Haveri district'),('Hazaribag','Hazaribag'),('Hingoli','Hingoli'),('Hissar','Hissar'),('Hooghly','Hooghly'),('Hoshangabad','Hoshangabad'),('Hoshiarpur','Hoshiarpur'),('Howrah','Howrah'),('Hyderabad','Hyderabad'),('Hyderabad','Hyderabad'),('Idukki','Idukki'),('Imphal East','Imphal East'),('Imphal West','Imphal West'),('Indore','Indore'),('Jabalpur','Jabalpur'),('Jagatsinghpur','Jagatsinghpur'),('Jaintia Hills','Jaintia Hills'),('Jaipur','Jaipur'),('Jaisalmer','Jaisalmer'),('Jajpur','Jajpur'),('Jalandhar','Jalandhar'),('Jalaun','Jalaun'),('Jalgaon','Jalgaon'),('Jalna','Jalna'),('Jalore','Jalore'),('Jalpaiguri','Jalpaiguri'),('Jammu','Jammu'),('Jamnagar','Jamnagar'),('Jamtara','Jamtara'),('Jamui','Jamui'),('Janjgir-Champa','Janjgir-Champa'),('Jashpur','Jashpur'),('Jaunpur district','Jaunpur district'),('Jehanabad','Jehanabad'),('Jhabua','Jhabua'),('Jhajjar','Jhajjar'),('Jhalawar','Jhalawar'),('Jhansi','Jhansi'),('Jharsuguda','Jharsuguda'),('Jhunjhunu','Jhunjhunu'),('Jind','Jind'),('Jodhpur','Jodhpur'),('Jorhat','Jorhat'),('Junagadh','Junagadh'),('Jyotiba Phule Nagar','Jyotiba Phule Nagar'),('Kabirdham (formerly Kawardha)','Kabirdham (formerly Kawardha)'),('Kadapa','Kadapa'),('Kaimur','Kaimur'),('Kaithal','Kaithal'),('Kakinada','Kakinada'),('Kalahandi','Kalahandi'),('Kamrup','Kamrup'),('Kamrup Metropolitan','Kamrup Metropolitan'),('Kanchipuram','Kanchipuram'),('Kandhamal','Kandhamal'),('Kangra','Kangra'),('Kanker','Kanker'),('Kannauj','Kannauj'),('Kannur','Kannur'),('Kanpur','Kanpur'),('Kanshi Ram Nagar','Kanshi Ram Nagar'),('Kanyakumari','Kanyakumari'),('Kapurthala','Kapurthala'),('Karaikal','Karaikal'),('Karauli','Karauli'),('Karbi Anglong','Karbi Anglong'),('Kargil','Kargil'),('Karimganj','Karimganj'),('Karimnagar','Karimnagar'),('Karnal','Karnal'),('Karur','Karur'),('Kasaragod','Kasaragod'),('Kathua','Kathua'),('Katihar','Katihar'),('Katni','Katni'),('Kaushambi','Kaushambi'),('Kendrapara','Kendrapara'),('Kendujhar (Keonjhar)','Kendujhar (Keonjhar)'),('Khagaria','Khagaria'),('Khammam','Khammam'),('Khandwa (East Nimar)','Khandwa (East Nimar)'),('Khargone (West Nimar)','Khargone (West Nimar)'),('Kheda','Kheda'),('Khordha','Khordha'),('Khowai','Khowai'),('Khunti','Khunti'),('Kinnaur','Kinnaur'),('Kishanganj','Kishanganj'),('Kishtwar','Kishtwar'),('Kodagu','Kodagu'),('Koderma','Koderma'),('Kohima','Kohima'),('Kokrajhar','Kokrajhar'),('Kolar','Kolar'),('Kolasib','Kolasib'),('Kolhapur','Kolhapur'),('Kolkata','Kolkata'),('Kollam','Kollam'),('Koppal','Koppal'),('Koraput','Koraput'),('Korba','Korba'),('Koriya','Koriya'),('Kota','Kota'),('Kottayam','Kottayam'),('Kozhikode','Kozhikode'),('Krishna','Krishna'),('Kulgam','Kulgam'),('Kullu','Kullu'),('Kupwara','Kupwara'),('Kurnool','Kurnool'),('Kurukshetra','Kurukshetra'),('Kurung Kumey','Kurung Kumey'),('Kushinagar','Kushinagar'),('Kutch','Kutch'),('Lahaul and Spiti','Lahaul and Spiti'),('Lakhimpur','Lakhimpur'),('Lakhimpur Kheri','Lakhimpur Kheri'),('Lakhisarai','Lakhisarai'),('Lalitpur','Lalitpur'),('Latehar','Latehar'),('Latur','Latur'),('Lawngtlai','Lawngtlai'),('Leh','Leh'),('Lohardaga','Lohardaga'),('Lohit','Lohit'),('Lower Dibang Valley','Lower Dibang Valley'),('Lower Subansiri','Lower Subansiri'),('Lucknow','Lucknow'),('Ludhiana','Ludhiana'),('Lunglei','Lunglei'),('Madhepura','Madhepura'),('Madhubani','Madhubani'),('Madurai','Madurai'),('Mahamaya Nagar','Mahamaya Nagar'),('Maharajganj','Maharajganj'),('Mahasamund','Mahasamund'),('Mahbubnagar','Mahbubnagar'),('Mahe','Mahe'),('Mahendragarh','Mahendragarh'),('Mahoba','Mahoba'),('Mainpuri','Mainpuri'),('Malappuram','Malappuram'),('Maldah','Maldah'),('Malkangiri','Malkangiri'),('Mamit','Mamit'),('Mandi','Mandi'),('Mandla','Mandla'),('Mandsaur','Mandsaur'),('Mandya','Mandya'),('Mansa','Mansa'),('Marigaon','Marigaon'),('Mathura','Mathura'),('Mau','Mau'),('Mayurbhanj','Mayurbhanj'),('Medak','Medak'),('Meerut','Meerut'),('Mehsana','Mehsana'),('Mewat','Mewat'),('Mirzapur','Mirzapur'),('Moga','Moga'),('Mokokchung','Mokokchung'),('Mon','Mon'),('Moradabad','Moradabad'),('Morena','Morena'),('Mumbai City','Mumbai City'),('Mumbai suburban','Mumbai suburban'),('Munger','Munger'),('Murshidabad','Murshidabad'),('Muzaffarnagar','Muzaffarnagar'),('Muzaffarpur','Muzaffarpur'),('Mysore','Mysore'),('Nabarangpur','Nabarangpur'),('Nadia','Nadia'),('Nagaon','Nagaon'),('Nagapattinam','Nagapattinam'),('Nagaur','Nagaur'),('Nagpur','Nagpur'),('Nainital','Nainital'),('Nalanda','Nalanda'),('Nalbari','Nalbari'),('Nalgonda','Nalgonda'),('Namakkal','Namakkal'),('Nanded','Nanded'),('Nandurbar','Nandurbar'),('Narayanpur','Narayanpur'),('Narmada','Narmada'),('Narsinghpur','Narsinghpur'),('Nashik','Nashik'),('Navsari','Navsari'),('Nawada','Nawada'),('Nawanshahr','Nawanshahr'),('Nayagarh','Nayagarh'),('Neemuch','Neemuch'),('Nellore','Nellore'),('New Delhi','New Delhi'),('Nilgiris','Nilgiris'),('Nizamabad','Nizamabad'),('North 24 Parganas','North 24 Parganas'),('North Delhi','North Delhi'),('North East Delhi','North East Delhi'),('North Goa','North Goa'),('North Sikkim','North Sikkim'),('North Tripura','North Tripura'),('North West Delhi','North West Delhi'),('Nuapada','Nuapada'),('Ongole','Ongole'),('Osmanabad','Osmanabad'),('Pakur','Pakur'),('Palakkad','Palakkad'),('Palamu','Palamu'),('Pali','Pali'),('Palwal','Palwal'),('Panchkula','Panchkula'),('Panchmahal','Panchmahal'),('Panchsheel Nagar district (Hapur)','Panchsheel Nagar district (Hapur)'),('Panipat','Panipat'),('Panna','Panna'),('Papum Pare','Papum Pare'),('Parbhani','Parbhani'),('Paschim Medinipur','Paschim Medinipur'),('Patan','Patan'),('Pathanamthitta','Pathanamthitta'),('Pathankot','Pathankot'),('Patiala','Patiala'),('Patna','Patna'),('Pauri Garhwal','Pauri Garhwal'),('Perambalur','Perambalur'),('Phek','Phek'),('Pilibhit','Pilibhit'),('Pithoragarh','Pithoragarh'),('Pondicherry','Pondicherry'),('Poonch','Poonch'),('Porbandar','Porbandar'),('Pratapgarh','Pratapgarh'),('Pratapgarh','Pratapgarh'),('Pudukkottai','Pudukkottai'),('Pulwama','Pulwama'),('Pune','Pune'),('Purba Medinipur','Purba Medinipur'),('Puri','Puri'),('Purnia','Purnia'),('Purulia','Purulia'),('Raebareli','Raebareli'),('Raichur','Raichur'),('Raigad','Raigad'),('Raigarh','Raigarh'),('Raipur','Raipur'),('Raisen','Raisen'),('Rajauri','Rajauri'),('Rajgarh','Rajgarh'),('Rajkot','Rajkot'),('Rajnandgaon','Rajnandgaon'),('Rajsamand','Rajsamand'),('Ramabai Nagar (Kanpur Dehat)','Ramabai Nagar (Kanpur Dehat)'),('Ramanagara','Ramanagara'),('Ramanathapuram','Ramanathapuram'),('Ramban','Ramban'),('Ramgarh','Ramgarh'),('Rampur','Rampur'),('Ranchi','Ranchi'),('Ratlam','Ratlam'),('Ratnagiri','Ratnagiri'),('Rayagada','Rayagada'),('Reasi','Reasi'),('Rewa','Rewa'),('Rewari','Rewari'),('Ri Bhoi','Ri Bhoi'),('Rohtak','Rohtak'),('Rohtas','Rohtas'),('Rudraprayag','Rudraprayag'),('Rupnagar','Rupnagar'),('Sabarkantha','Sabarkantha'),('Sagar','Sagar'),('Saharanpur','Saharanpur'),('Saharsa','Saharsa'),('Sahibganj','Sahibganj'),('Saiha','Saiha'),('Salem','Salem'),('Samastipur','Samastipur'),('Samba','Samba'),('Sambalpur','Sambalpur'),('Sangli','Sangli'),('Sangrur','Sangrur'),('Sant Kabir Nagar','Sant Kabir Nagar'),('Sant Ravidas Nagar','Sant Ravidas Nagar'),('Saran','Saran'),('Satara','Satara'),('Satna','Satna'),('Sawai Madhopur','Sawai Madhopur'),('Sehore','Sehore'),('Senapati','Senapati'),('Seoni','Seoni'),('Seraikela Kharsawan','Seraikela Kharsawan'),('Serchhip','Serchhip'),('Shahdol','Shahdol'),('Shahjahanpur','Shahjahanpur'),('Shajapur','Shajapur'),('Shamli','Shamli'),('Sheikhpura','Sheikhpura'),('Sheohar','Sheohar'),('Sheopur','Sheopur'),('Shimla','Shimla'),('Shimoga','Shimoga'),('Shivpuri','Shivpuri'),('Shopian','Shopian'),('Shravasti','Shravasti'),('Sibsagar','Sibsagar'),('Siddharthnagar','Siddharthnagar'),('Sidhi','Sidhi'),('Sikar','Sikar'),('Simdega','Simdega'),('Sindhudurg','Sindhudurg'),('Singrauli','Singrauli'),('Sirmaur','Sirmaur'),('Sirohi','Sirohi'),('Sirsa','Sirsa'),('Sitamarhi','Sitamarhi'),('Sitapur','Sitapur'),('Sivaganga','Sivaganga'),('Siwan','Siwan'),('Solan','Solan'),('Solapur','Solapur'),('Sonbhadra','Sonbhadra'),('Sonipat','Sonipat'),('Sonitpur','Sonitpur'),('South 24 Parganas','South 24 Parganas'),('South Delhi','South Delhi'),('South Garo Hills','South Garo Hills'),('South Goa','South Goa'),('South Sikkim','South Sikkim'),('South Tripura','South Tripura'),('South West Delhi','South West Delhi'),('Sri Muktsar Sahib','Sri Muktsar Sahib'),('Srikakulam','Srikakulam'),('Srinagar','Srinagar'),('Subarnapur (Sonepur)','Subarnapur (Sonepur)'),('Sultanpur','Sultanpur'),('Sundergarh','Sundergarh'),('Supaul','Supaul'),('Surat','Surat'),('Surendranagar','Surendranagar'),('Surguja','Surguja'),('Tamenglong','Tamenglong'),('Tarn Taran','Tarn Taran'),('Tawang','Tawang'),('Tehri Garhwal','Tehri Garhwal'),('Thane','Thane'),('Thanjavur','Thanjavur'),('The Dangs','The Dangs'),('Theni','Theni'),('Thiruvananthapuram','Thiruvananthapuram'),('Thoothukudi','Thoothukudi'),('Thoubal','Thoubal'),('Thrissur','Thrissur'),('Tikamgarh','Tikamgarh'),('Tinsukia','Tinsukia'),('Tirap','Tirap'),('Tiruchirappalli','Tiruchirappalli'),('Tirunelveli','Tirunelveli'),('Tirupur','Tirupur'),('Tiruvallur','Tiruvallur'),('Tiruvannamalai','Tiruvannamalai'),('Tiruvarur','Tiruvarur'),('Tonk','Tonk'),('Tuensang','Tuensang'),('Tumkur','Tumkur'),('Udaipur','Udaipur'),('Udalguri','Udalguri'),('Udham Singh Nagar','Udham Singh Nagar'),('Udhampur','Udhampur'),('Udupi','Udupi'),('Ujjain','Ujjain'),('Ukhrul','Ukhrul'),('Umaria','Umaria'),('Una','Una'),('Unnao','Unnao'),('Upper Siang','Upper Siang'),('Upper Subansiri','Upper Subansiri'),('Uttar Dinajpur','Uttar Dinajpur'),('Uttara Kannada','Uttara Kannada'),('Uttarkashi','Uttarkashi'),('Vadodara','Vadodara'),('Vaishali','Vaishali'),('Valsad','Valsad'),('Varanasi','Varanasi'),('Vellore','Vellore'),('Vidisha','Vidisha'),('Viluppuram','Viluppuram'),('Virudhunagar','Virudhunagar'),('Visakhapatnam','Visakhapatnam'),('Vizianagaram','Vizianagaram'),('Vyara','Vyara'),('Warangal','Warangal'),('Wardha','Wardha'),('Washim','Washim'),('Wayanad','Wayanad'),('West Champaran','West Champaran'),('West Delhi','West Delhi'),('West Garo Hills','West Garo Hills'),('West Kameng','West Kameng'),('West Khasi Hills','West Khasi Hills'),('West Siang','West Siang'),('West Sikkim','West Sikkim'),('West Singhbhum','West Singhbhum'),('West Tripura','West Tripura'),('Wokha','Wokha'),('Yadgir','Yadgir'),('Yamuna Nagar','Yamuna Nagar'),('Yanam','Yanam'),('Yavatmal','Yavatmal'),('Zunheboto','Zunheboto')]


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

    maritalChoices = [('Single' , 'Single') , ('Divorced' , 'Divorced') , ('Widow' , 'Widow/Widower') , ('Poly' , 'Believe in Polygamy')]
    first_name = StringField('First Name', validators = [InputRequired()])
    last_name = StringField('Last Name', validators = [Optional()])
    gender = SelectField('Gender', choices = genderChoices)
    dob = DateField('Date of Birth', validators = [InputRequired()])
    marital_status = SelectField('Marital Status' , choices = maritalChoices , validators = [InputRequired()])
    hometown = SelectField('Hometown', choices = cities, validators = [Optional()])
    mother_tongue = SelectField('Mother Tongue',choices = langs, validators = [Optional()])
    about = TextField('About', validators = [Optional()])
    current_location = SelectField('Current Location', choices = cities, validators = [Optional()])
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
    salary = StringField('Salary (Enter range)' , validators = [Optional()])
    hometown = SelectField('Hometown', choices = cities, validators = [Optional()])
    height = StringField('Height (Enter range in cm)' , validators = [Optional()])
    current_location = SelectField('Current Location', choices = cities, validators = [Optional()])
    gender = SelectField('Gender', choices = genderChoices)
    mother_tongue = SelectField('Mother Tongue', choices = langs, validators = [Optional()])
    about = TextField('About', validators = [Optional()])
    submit = SubmitField('Save Changes')
    skip = SubmitField('Skip')

class EditSocialMediaForm(Form):

    facebook = StringField('Facebook Link', validators = [Optional()], default = "https://www.facebook.com/")
    twitter = StringField('Twitter Link', validators = [Optional()],default = "https://www.twitter.com/")
    instagram = StringField('Instagram Link', validators = [Optional()],default = "https://www.instagram.com/")
    linkedin = StringField('Linkedin Link', validators = [Optional()],default = "https://www.linkedin.com/in/")
    submit = SubmitField('Save and Next')
    skip = SubmitField('Skip')

class EditImageGalleryForm(Form):

    image = FileField('Upload Picture(s)', validators=[myvalidator, Optional() , FileAllowed(images, 'Image only!')])
    submit = SubmitField('Save and Next')
    skip = SubmitField('Skip')

class EditBodyForm(Form):

    skinChoices = [('Pale','Pale'),('Fair','Fair'), ('Brown' , 'Brown') , ('Dark' , 'Dark')]
    hairChoices = [('Black','Black'), ('Brown','Brown'),('Blonde','Blonde'),('Red','Red'),('White','White'), ]
    height = IntegerField('Height(in cm)' , validators = [Optional()])
    weight = IntegerField('Weight' , validators = [Optional()])
    hair_colour = SelectField('Hair Colour', validators = [Optional()] ,  choices = hairChoices)
    complexion = SelectField('Complexion' , choices = skinChoices)
    submit = SubmitField('Save and Next')
    skip = SubmitField('Skip')

class DeleteProfileForm(Form):
    email = StringField('E-mail', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Confirm')

class SearchFilterForm(Form):
    age_lower = IntegerField('Lower Limit of Age' , validators = [Optional()])
    age_upper = IntegerField('Upper Limit of Age' , validators = [Optional()])
    gender = SelectField('Gender', choices = genderChoices)
    mother_tongue = SelectField('Mother Tongue', choices = langs,  validators = [Optional()])
    current_location = SelectField('Current Location', choices = cities, validators = [Optional()])
    hometown = SelectField('Hometown',choices= cities, validators = [Optional()])
    occupation = StringField('Occupation', validators = [Optional()])
    height = IntegerField('Lower Limit of Height(in cm)' , validators = [Optional()])
    salary = IntegerField('Lower Limit of Salary' , validators = [Optional()])
    under_grad = StringField('Under Graduation', validators = [Optional()])
    post_grad = StringField('Post Gradution', validators = [Optional()])
    submit = SubmitField('Search')


class SendMessageForm(Form):
    subject = StringField('Subject')
    body = TextField('Body')
    submit = SubmitField('Send')

class ProposalForm(Form):
    toUser = StringField('Partner Username', validators =[DataRequired()])
    submit = SubmitField('Submit')

class QuickSearchForm(Form):
    username = StringField('Quick Search ', validators =[DataRequired()])
    submit = SubmitField('Submit')

class CreateStoryForm(Form):
    story = TextField('Add your Story', validators = [DataRequired()])
    submit = SubmitField('Submit')







