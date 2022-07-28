from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "noura"
password = "123"
facebook_friends=["beb","Yonathan","Adan", "George", "Fouad", "Celina"]
name = "yaso"

@app.route('/',methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		if username == request.form['username'] and password == request.form['password']:
			return redirect(url_for('Home'))
		else:
			return render_template('login.html')
	return render_template('login.html')

@app.route('/home')
def Home():
	return render_template('home.html',friends=facebook_friends)

@app.route('/friend_exists/<string:name>',methods=['GET', 'POST'])
def Friends(name):
    if name in facebook_friends:
    	boolean = 'TRUE'
    	return render_template('friend_exists.html', n = name, b = boolean)
        


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)