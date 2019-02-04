from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = TRUE


@app.route("/")
def index():
    

app.run()