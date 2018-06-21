from flask import render_template
from app import app

@app.route('/')
@app.route('/index')  
def index():
	user = {'username': 'Antonio'}
	events = [
		{
			'name': 'Antonio', 
			'date': '111111111111'
		},
		{
			'name': 'Qiqe',
			'date': '1111111111111'
		}
	]
	return render_template('index.html', user=user, title='Testigos', events=events)