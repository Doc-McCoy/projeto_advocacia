from flask_login import UserMixin
from shared.db import db

class Usuarios(UserMixin, db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    nome            = db.Column(db.String(255), nullable=False)
    email           = db.Column(db.String(255), nullable=False, unique=True)
    senha           = db.Column(db.String(255), nullable=False)
    departamento    = db.Column(db.Integer, nullable=False)
