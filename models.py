from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    cognome = db.Column(db.String(80))
    scuola = db.Column(db.String(120))
    classe = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, nullable=False)
    presenze = db.relationship("Presenza", backref="user", lazy=True)


class Presenza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(255))
