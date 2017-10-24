WTF_CSRF_ENABLED = True
SECRET_KEY = 'wedx-secret-key'
SQLALCHEMY_DATABASE_URI = 'mysql://root:aravindbs@localhost:3306/wedx'
#SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/wedx'
UPLOADS_DEFAULT_DEST = 'app/static/img/'
UPLOADS_DEFAULT_URL = '../static/img/'
UPLOADED_IMAGES_ALLOW = set(['png', 'jpg', 'jpeg'])

UPLOADED_IMAGES_DEST ='app/static/img/'
UPLOADED_IMAGES_URL = '../static/img/'
