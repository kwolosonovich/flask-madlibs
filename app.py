#import flask and access to requests
from flask import Flask, request

@app.route('/')
def index():
    """Return homepage."""
    return render_template("home.html")