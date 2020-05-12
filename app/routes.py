from random import*

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
from werkzeug.urls import url_parse

interests = []
sessions = 0
remainder = 0


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
    global sessions
    global remainder
    hours = 0
    minutes = 0
    if 'hours' in request.args:
        hours = request.args.get('hours')
    if 'minutes' in request.args:
        minutes = request.args.get('minutes')
        hours = int(hours)
        minutes = int(minutes)
        sessions = (((hours * 60) + minutes) / 80) * 1000
        remainder = ((sessions % 1000)/1000)*80
        remainder = int(remainder)
        sessions = sessions / 1000
        sessions = int(sessions)
        sessions = sessions+1

    sessions = sessions - 1
    if sessions == 0:
        if sessions < 0:
            return render_template('setup.html', title='Setup')
        else:
            return render_template('work.html', title='Work', values=[0, remainder, 0])
    else:
        return render_template('work.html', title='Work', values=[1, 0, 1])


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
    min = request.args.get('min2')
    sec = request.args.get('sec2')
    loadBreaks()
    currentbr = chooseBreak()
    if currentbr.type == "youtube":
        current = currentbr.content[0]
        return render_template('videoBreak.html', title='Break', content=current, values=[min, sec])
    elif currentbr.type == "combo":
        cont1 = currentbr.content[0]
        cont2 = currentbr.content[1]
        cont3 = currentbr.content[2]
        return render_template('comboBreak.html', title='Break', content1=cont1, content2=cont2, content3=cont3, values=[min, sec])
    else:
        current = currentbr.content[0]
        cont2 = currentbr.content[1]
        return render_template('textBreak.html', title='Break', content1=current, content2=cont2, values=[min, sec])

class Break:
    def __init__(fun, interest, type, content):
        fun.interest = interest
        fun.type = type
        fun.content = content


breaks = []


def loadBreaks():
    thing1 = Break("Music", "youtube", ["https://www.youtube.com/embed/1YAf8hFX0M0"])
    breaks.append(thing1)
    thing2 = Break("Music", "youtube", ["https://www.youtube.com/embed/DX5_o-mumvE"])
    breaks.append(thing2)
    break2 = Break("Music", "article", [
        "https://www.npr.org/2020/02/21/807821340/the-lessons-to-be-learned-from-forcing-plants-to-play-music", "The Lessons To Be Learned From Forcing Plants To Play Music"])
    breaks.append(break2)

    break1 = Break("Cooking", "youtube", ["https://www.youtube.com/embed/bIqUT78mnvg"])
    breaks.append(break1)
    break3 = Break("Cooking", "article", ["this is content", "Article title"])
    breaks.append(break3)
    break5 = Break("Cooking", "youtube", ["https://www.youtube.com/embed/CE3OutlMcfM"])
    breaks.append(break5)
    break6 = Break("Cooking", "youtube", ["https://www.youtube.com/embed/-7i9dTJgsdI"])
    breaks.append(break6)
    break7 = Break("Cooking", "combo", ["https://www.youtube.com/embed/NN-bLP2B8f4", "https://diyjoy.com/easy-snacks-recipes/", "43 Easy Snacks You Can Make In Less Than 5 Minutes"])
    breaks.append(break7)
    break8 = Break("Cooking", "youtube", ["https://www.youtube.com/embed/1Gdl-A1DvpA"])
    breaks.append(break8)

    break9 = Break("Photography", "youtube", ["https://www.youtube.com/embed/ineZXLbL7s8"])
    breaks.append(break9)
    break10 = Break("Photography", "youtube", ["https://www.youtube.com/embed/PW8tr4j1ZWE"])
    breaks.append(break10)
    break11 = Break("Photography", "article", ["https://www.nationalgeographic.com/photography/photo-tips/digital-photography-tips/", "Digital Photography Tips"])
    breaks.append(break11)

    break12 = Break("History", "article",
                    ["https://www.nytimes.com/2020/04/27/world/europe/russia-historian-stalin-mass-graves.html?action=click&module=Top%20Stories&pgtype=Homepage", "He Found One of Stalin’s Mass Graves. Now He’s in Jail."])
    breaks.append(break12)
    break13 = Break("History", "youtube", ["https://www.youtube.com/embed/BEG-ly9tQGk"])
    breaks.append(break13)


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
