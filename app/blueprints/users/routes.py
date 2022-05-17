from flask import render_template, current_app as app

@app.route('/login')
def login():
    return render_template('users/login.html')

@app.route('/register')
def register():
    return render_template('users/register.html')
