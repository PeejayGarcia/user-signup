from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

# Define error conditions

def val_username(new_username):
    if len(new_username) < 1:
        username_error = "Username field cannot be blank."
    elif len(new_username) < 3 or len(new_username) > 20:
        username_error = "That is not a valid username."
    elif ' ' in new_username:
        username_error = "Username cannot contain spaces."
    else:
        username_error = ""
    return username_error

def val_password(new_password):
    if len(new_password) < 1:
        password_error = "Password field cannot be blank."
    elif len(new_password) <3 or len(new_password) >20:
        password_error = "That is not a valid password."
    elif ' ' in new_password:
        password_error = "Password cannot contain spaces"
    else:
        password_error = ""
    return password_error

def val_verify_password(new_password, match):
    if new_password != match or len(match) == 0:
        match_error = "Your Passwords do not match."
    else:
        match_error = ""
    return match_error

@app.route('/', methods=['POST'])
def welcome():
    newusername = request.form['new-username']
    newpassword = request.form['new-password']
    matchpassword = request.form['match-password']

    username_err = val_username(newusername)
    password_err = val_password(newpassword)
    match_err = val_verify_password(newpassword, matchpassword)
    
    if username_err == "" and password_err == "" and match_err == "":
        template = jinja_env.get_template('welcome.html')
        return template.render(new_username=newusername)
    
    template = jinja_env.get_template('index.html')
    return template.render(username_error=username_err, password_error=password_err,
    match_error=match_err, new_username=newusername)

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()


app.run()