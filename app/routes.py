from random import random

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
from werkzeug.urls import url_parse



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


interests = []


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

def goToSetupPage(form):
    for x in range(4):
        name= "checkbox"+str(x+1)
        if form.name.checked:
            interests.append(form.name.value)
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
    loadBreaks()
    current = chooseBreak()
    return render_template('break.html', title='Break', content=current.content)


class Break:
    def __init__(fun, interest, type, content):
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