from flask import Flask, redirect, request, render_template, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "lol123"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration', methods=['POST'])
def registration():
    session['first_name'] = str(request.form['first_name'])
    session['lastname'] = str(request.form['last_name'])
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']

    if len(session['first_name']) < 1:
        flash("Please put a First Name", 'error')
        if session['first_name'].isalpha() != True:
            flash("First Name must only containt letters", 'error')

    if len(session['lastname']) < 1:
		flash("Please put a Last Name", 'error')
		if session['lastname'] != True:
			flash("Last name must only contain letters.", 'error')

    if len(session['email']) < 1:
		flash("Please put an email", 'error')
		if not EMAIL_REGEX.match(request.form['email']):
			flash("Invalid Email Address!")

    if len(session['password']) < 1:
        flash("Please put a paswword", 'error')

    if len(session['confirm']) < 1:
        flash("Please confirm password", 'error')

    if len(session['password']) < 8:
        flash("Password must contain minimum of 8 characters.", 'error')
        if session['password'] != session['confirm']:
            flash("Passwords must match.", 'error')

    else:
		flash("Success", 'no_errors')

    return redirect('/')

@app.route('/reset')
def reset():
	print "Clear"
	session.clear()
	return redirect('/')

app.run(debug=True)
