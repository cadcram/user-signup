from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/", methods=["POST"])
def validate_inputs():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_pass_error = ''
    email_error = ''

    # if-statement to return correct error message for username
    if len(username) == 0:
        username_error = 'Please Enter A Username'
        username = ''
    elif len(username) < 3:
        username_error = "Username must be longer than 3 characters"
        username = ''
    elif len(username) > 20:
        username_error = "Username must be shorter than 20 characters."
        username = ''
    else:
        #I don't know if I have to end with an 'else' but just for fun at this point :)
        username = username

    # if-statement to return correct error message for password
    if len(password) == 0:
        password_error = 'Please Enter A Password'
        password = ''
    elif len(password) < 3:
        password_error = "Password must be longer than 3 characters"
        password = ''
    elif len(password) > 20:
        password_error = "Password must be shorter than 20 characters."
        password = ''
    else:
        #I don't know if I have to end with an 'else' but just for fun at this point :)
        password = password

    # if-statement to return correct error message for verify password
    if verify_password != password:
        verify_pass_error = 'Password and Password Verification Do Not Match.'
        verify_password = ''
    
    # if-statment to return correct error message for the optional email
    if email != "":
        if len(email) < 3:
            email_error = "Email must be longer than 3 characters."
            email = ''
        elif len(email) > 20:
            email_error = " Email must be shorter than 20 characters."
            email = ''
        elif '@' not in email:
            email_error = "Email must contain '@' "
            email = ''
        elif '.' not in email:
            email_error = "Email must contain '.' "
            email = ''
    
    # if-statment to check if there are any errors and redirect accordingly
    if not username_error and not password_error and not verify_pass_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html',
            username_error=username_error,
            password_error=password_error,
            verify_pass_error=verify_pass_error,
            email_error=email_error)


   

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', title="Welcome!", username=username)

app.run()