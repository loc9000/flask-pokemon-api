from app import app

@app.route('/')
def home():
    return "Home Page"

@app.route('/login')
def login():
    return "Log in Page"

@app.route('/register')
def register():
    return "Register Page"