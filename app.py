from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'wedx'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route("/")
def main():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')
@app.route('/signUp', methods=['POST'])
def signUp():
	try:
	#read values posted in the UI
		_username = request.form['inputUsername']
		_fname = request.form['inputFName']
		_lname = request.form['inputLName']
		_password = request.form['inputPassword']

		#validate the receieved values

		if _username and _fname and _lname and _password:

			conn = mysql.conect()
			cursor = conn.cursor()
			_hashed_password = generate_password_hash(_password)
			cursor.callproc('sp_createUser', (_fname, _lname, _username, _hashed_password))
			data = cursor.fetchall()

			if len(data) is 0:
				conn.commit()
				return json.dumps({'message':"User created successfully"})

			else:
				return json.dumps({'error': str(data[0])})

		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})

	except Exception as e:
		return json.dumps({'error':str(e)})

	finally:
		cursor.close()
		conn.close()





if __name__=="__main__":
	app.run()
