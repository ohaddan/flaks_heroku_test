from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ted','Pet': 'Frog'}
    return render_template('index.html',
                           title='Home',
                           color='red',
                           user=user)


@app.route('/adv')
def advanced_rendering():
	users = [
		{'name':'Ted', 'food':'Pizza'},
		{'name':'Naomi', 'food':'Bagels'},
		{'name':'MEET', 'food':'Nutella'}
		]
	return render_template('adv_rendering.html',
		title='My pretty website',
		users = users)

@app.route('/challange')
def challange():
	numbers = list(range(-10, 10))
	return render_template('challange.html',
		numbers = numbers)