from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	return "hi :) my name is Bob this is a good day"
