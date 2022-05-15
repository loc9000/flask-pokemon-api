from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('main/home.html')

@app.route('/login')
def login():
    return "Log in Page"

@app.route('/register')
def register():
    return "Register Page"