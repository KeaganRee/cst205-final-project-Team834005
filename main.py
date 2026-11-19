#main python file
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
import pickle
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'

bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signIn():
    return render_template('signin.html')

@app.route('/artists')
def artists():
    return render_template('artists.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

@app.route('/playlist')
def playlist():
    return render_template('playlist.html')