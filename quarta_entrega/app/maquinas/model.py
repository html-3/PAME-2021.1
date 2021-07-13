from app.extensions import db
from datetime import date

class Maquina(db.Model):

    data_base = date(2021, 1, 1)

    id = db.Column(db.Integer, primary_key=True)

    modelo = db.Column(db.String(50), nullable=False)

    implementacao = db.Column(db.String(30), default=data_base)

    #funcionarios_id = db.relationship("Maquina", backref='operador', lazy=True)