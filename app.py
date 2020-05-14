#import flask and access to requests
from flask import Flask, request
from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route('/')
def index():
    """Return homepage with questions form story"""
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)

@app.route('/story')
def my_stories():
    """stories page"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)