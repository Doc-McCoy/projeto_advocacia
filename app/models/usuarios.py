from shared.db import db

class Usuarios(db.Model):
    usu_id              = db.Column(db.Integer, primary_key=True)
    usu_nome            = db.Column(db.String(80), nullable=False)
    usu_email           = db.Column(db.String(80), nullable=False, unique=True)
    usu_senha           = db.Column(db.String(120), nullable=False)
    usu_departamento    = db.Column(db.Integer, nullable=False)
