import uuid
from datetime import datetime as dt
from app import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    type = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    owner = db.Column(db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Pokemon: {self.name}>'

class User(db.Model):
    id = db.Column(db.String(32), default=uuid.uuid4().hex, primary_key=True)
    first_name = db.Column(db.String[50])
    last_name = db.Column(db.String[50])
    email = db.Column(db.String[50], unique=True)
    password = db.Column(db.String(300))
    pokemon = db.relationship('Pokemon', backref='pokemon', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User: {self.email}>'