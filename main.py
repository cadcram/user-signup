from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/", methods=["POST"])

@app.route("/welcome")
def welcome():
    welcome = request.args.get('username')
    return render_template('welcome.html', title="Welcome!", username=username)