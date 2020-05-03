from random import random

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
from werkzeug.urls import url_parse


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


interests = []


@app.route('/goToSetupPage', methods=['GET', 'POST'])
def goToSetupPage(form):
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
    loadBreaks()
    current = chooseBreak()
    return render_template('break.html', title='Break', content=current.content)


class Break:
    def __init__(fun, type, content):
        fun.type = type
        fun.content = content


breaks = []


def loadBreaks():
    thing1 = Break("music", "https://www.youtube.com/watch?v=1YAf8hFX0M0")
    breaks.append(thing1)


def chooseBreak():
    if len(interests) == 0:
        interests.append("music")
    if len(interests) > 1:
        interest = getRandNum(len(interests))
    else:
        interest = 0
    strInterest= interests[interest]
    possible= []
    for x in breaks:
        if breaks[x].type == strInterest:
            possible.append(breaks[x])

    theBreak= possible[getRandNum(len(possible))]
    return theBreak


def getRandNum(range):
    return random.randrange(0, range)