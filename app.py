from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

def signUp():
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request['inputPassword']

	

if __name__=="__main__":
	app.run()
