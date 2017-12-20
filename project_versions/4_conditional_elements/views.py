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
    return render_template('adv_rendering.html',
                           title=None)

    