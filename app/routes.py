from app import app, db
from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home')

@app.route('/goToHomePage', methods=['GET', 'POST'])
def goToHomePage():
    return render_template('index.html', title='Home')

@app.route('/goToSciencePage', methods=['GET', 'POST'])
def goToSciencePage():
    return render_template('science.html', title='Science')

@app.route('/goToSetupPage', methods=['GET', 'POST'])
def goToSetupPage(form):
    interests= []
    for x in range(4):
        name= "checkbox"+str(x+1)
        if form.name.checked:
            interests.append(form.name.value)
    return render_template('setup.html', title='Setup')

@app.route('/goToWorkPage', methods=['GET', 'POST'])
def goToWorkPage():
    total_time = request.args.get('total_time')
    often = request.args.get('often')
    print("THE TOTAL TIME: " + total_time)
    print("HOW OFTEN A BREAK: " + often)
    return render_template('work.html', title='Work')


@app.route('/goToBreakPage', methods=['GET', 'POST'])
def goToBreakPage():
    return render_template('break.html', title='Break')

class Break:
    def __init__(fun, type, content):
        fun.type = type
        fun.content = content

