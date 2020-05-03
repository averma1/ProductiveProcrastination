from app import app, db
from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm
from app.models import User


interests= []
totalTime = 0
often = 0

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
def goToSetupPage():

    interest1 = request.args.get('interest1')
    if interest1 != None:
        print(interest1)
        interests.append(interest1)

    interest2 = request.args.get('interest2')
    if interest2 != None:
        print(interest2)
        interests.append(interest2)

    interest3 = request.args.get('interest3')
    if interest3 != None:
        print(interest3)
        interests.append(interest3)

    interest4 = request.args.get('interest4')
    if interest4 != None:
        print(interest4)
        interests.append(interest4)

    return render_template('setup.html', title='Setup')

@app.route('/goToWorkPage', methods=['GET', 'POST'])
def goToWorkPage():
    global totalTime
    global often
    if 'total_time' in request.args:
        totalTime = request.args.get('total_time')
    if 'often' in request.args:
        often = request.args.get('often')
    print("THE TOTAL TIME: " + totalTime)
    print("HOW OFTEN A BREAK: " + often)
    return render_template('work.html', title='Work', values = [totalTime, often])


@app.route('/goToBreakPage', methods=['GET', 'POST'])
def goToBreakPage():
    break_items = []
    break1 = Break("cooking", "youtube", "https://www.youtube.com/embed/bIqUT78mnvg")
    break_items.append(break1)
    break2 = Break("cooking", "article copy", "this is content")
    break_items.append(break2)
    break3 = Break("cooking", "youtube", "this is content")
    break_items.append(break3)
    break4 = Break("cooking", "youtube", "this is content")
    break_items.append(break4)
    break5 = Break("cooking", "youtube", "this is content")
    break_items.append(break5)
    break6 = Break("cooking", "youtube", "this is content")
    break_items.append(break6)
    break7 = Break("cooking", "youtube", "this is content")
    break_items.append(break7)
    return render_template('break.html', title='Break', breaks=break_items)

class Break:
    def __init__(fun, interest, type, content):
        fun.interest = interest
        fun.type = type
        fun.content = content

