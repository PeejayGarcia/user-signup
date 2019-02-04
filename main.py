from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/username", methods=['POST'])
def add_username():
    new_username = request.form['new-username']

    if (not new_username) or (new_username.strip() ==""):
        error =  "Please specify a valid Username."
        return redirect("/?error=" + error)

    if (not new_username) or (new_username.strip() ==""):
        error =  "Please specify a valid Username."
        return redirect("/?error=" + error)

    return render_template('welcome.html', name=new_username)

@app.route("/username", methods=['POST'])
def add_password():
    new_password = request.form['new-password']

    if (not new_password) or (new_password.strip() ==""):
        error =  "Please specify a valid Password."
        return redirect("/?error=" + error)

    return render_template('welcome.html')

@app.route("/username", methods=['POST'])
def verify_password():
    verified_password = request.form['verified-password']

    if (not verified_password) or (verified_password.strip() ==""):
        error =  "Your passwords don't match."
        return redirect("/?error=" + error)
    return render_template('welcome.html')



@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html', error=encoded_error and cgi.escape(encoded_error, quote=True))


app.run()