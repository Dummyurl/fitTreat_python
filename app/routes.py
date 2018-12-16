from flask import render_template, redirect, url_for
from app import app

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/home')
def home():
    user = {'username': 'Saurabh'}
    return render_template('home.html', title='Home', user=user)