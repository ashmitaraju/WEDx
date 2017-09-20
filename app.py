from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')
@app.route('/signUp', methods=['POST'])
def signUp():
	#read values posted in the UI
	_username = request.form['inputUsername']
	_fname = request.form['inputFName']
	_lname = request.form['inputLName']
	_password = request.form['inputPassword']

	#validate the receieved values

	if _username and _fname and _lname and _password:
		return json.dumps({'html':'<span>All fields good !!</span>'})

	else:
		 return json.dumps({'html':'<span>Enter the required fields</span>'})




if __name__=="__main__":
	app.run()
