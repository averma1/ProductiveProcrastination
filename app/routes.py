from app import app

@app.route('/')
@app.route('/index')
def index():
	return "hi :) my name is Bob this is a good day"
