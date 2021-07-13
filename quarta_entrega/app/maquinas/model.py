from app.extensions import db
from datetime import datetime

class Maquina(db.Model):

    data_base = datetime(2021, 1, 1)

    id = db.Column(db.Integer, primary_key=True)

    modelo = db.Column(db.String(50), nullable=False)

    implementacao = db.Column(db.DateTime, default=data_base)

    #funcionarios_id = db.relationship("Maquina", backref='operador', lazy=True)