from random import*

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
from werkzeug.urls import url_parse

interests = []
totalTime = 0
often = 0


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='About Us')

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
    return render_template('work.html', title='Work', values=[totalTime, often])


@app.route('/goToBreakPage', methods=['GET', 'POST'])
def goToBreakPage():
    loadBreaks()
    currentbr = chooseBreak()
    if currentbr.type == "youtube":
        current = currentbr.content[0]
        return render_template('videoBreak.html', title='Break', content=current, values=[19, 60])
    elif currentbr.type == "combo":
        cont1 = currentbr.content[0]
        cont2 = currentbr.content[1]
        return render_template('comboBreak.html', title='Break', content1=cont1, content2=cont2, values=[19, 60])
    else:
        current = currentbr.content[0]
        return render_template('textBreak.html', title='Break', content=current, values=[19, 60])


@app.route('/refreshBreakPage', methods=['GET', 'POST'])
def refreshBreakPage():
    min = request.args.get('minutes2')
    sec = request.args.get('seconds2')
    loadBreaks()
    currentbr = chooseBreak()
    if currentbr.type == "youtube":
        current = currentbr.content[0]
        return render_template('videoBreak.html', title='Break', content=current, values=[min, sec])
    elif currentbr.type == "combo":
        cont1 = currentbr.content[0]
        cont2 = currentbr.content[1]
        return render_template('comboBreak.html', title='Break', content1=cont1, content2=cont2, values=[min, sec])
    else:
        current = currentbr.content[0]
        return render_template('textBreak.html', title='Break', content=current, values=[min, sec])

class Break:
    def __init__(fun, interest, type, content):
        fun.interest = interest
        fun.type = type
        fun.content = content


breaks = []


def loadBreaks():
    thing1 = Break("Music", "youtube", ["https://www.youtube.com/embed/1YAf8hFX0M0"])
    break1 = Break("Cooking", "youtube", ["https://www.youtube.com/embed/bIqUT78mnvg"])
    breaks.append(break1)
    break2 = Break("Cooking", "article", ["this is content"])
    breaks.append(break2)
    break3 = Break("Cooking", "article", ["this is content"])
    breaks.append(break3)
    break4 = Break("Cooking", "article", ["this is content"])
    breaks.append(break4)
    break5 = Break("Cooking", "youtube", ["https://www.youtube.com/embed/CE3OutlMcfM"])
    breaks.append(break5)
    break6 = Break("Cooking", "youtube", ["https://www.youtube.com/embed/-7i9dTJgsdI"])
    breaks.append(break6)
    break7 = Break("Cooking", "combo", ["https://www.youtube.com/embed/NN-bLP2B8f4", "this is content"])
    breaks.append(break7)
    breaks.append(thing1)


def chooseBreak():
    if len(interests) == 0:
        interests.append("Music")
    if len(interests) > 1:
        interest = getRandNum(len(interests))
    else:
        interest = 0
    strInterest= interests[interest]
    possible= []
    for x in breaks:
        if x.interest == strInterest:
            possible.append(x)

    theBreak= possible[getRandNum(len(possible))]
    return theBreak


def getRandNum(range):
    return int(random()*range)
