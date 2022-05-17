from flask import render_template, current_app as app
from datetime import datetime as dt

@app.route('/')
def home():

    pokemon_list = [
        {
            'name': 'Pokemon name', 
            'description': 'pokemon description',
            'type': 'pokemon type',
            'date_created': dt.utcnow()
        },
        {
            'name': 'Pokemon name', 
            'description': 'pokemon description',
            'type': 'pokemon type',
            'date_created': dt.utcnow()
        },
        {
            'name': 'Pokemon name', 
            'description': 'pokemon description',
            'type': 'pokemon type',
            'date_created': dt.utcnow()
        }
    ]
    return render_template('main/home.html', pokemon=pokemon_list)

@app.route('/pokedex')
def pokedex():
    return render_template('main/pokedex.html')


