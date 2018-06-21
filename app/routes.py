from flask import render_template
from app import app

@app.route('/')
@app.route('/index')  
def index():
	user = {'username': 'Antonio'}
	events = [
		{
			'name': 'Antreq', 
			'date': '9167 3960 9126'
		},
		{
			'name': 'Qiqe',
			'date': '1709 5990 0028'
		}
		{
			'name': 'Saurios21',
			'date': '1189 7617 0817'
		}
	]
	return render_template('index.html', user=user, title='Testigos', events=events)