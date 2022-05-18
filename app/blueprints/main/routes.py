from flask import render_template, current_app as app
from datetime import datetime as dt
from app.blueprints.main.models import Pokemon

@app.route('/')
def home():
    return render_template('main/home.html', pokemon=Pokemon.query.all())

@app.route('/pokedex')
def pokedex():
    return render_template('main/pokedex.html')


