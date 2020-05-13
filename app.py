#import flask and access to requests
from flask import Flask, request
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route('/')
def index():
    """Return homepage."""
    return render_template("home.html")

@app.route('/stories')
def my_stories():
    """stories page"""
    return render_template("stories.html")