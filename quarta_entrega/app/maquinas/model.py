from app.extensions import db
from datetime import date

class Maquina(db.Model):

    data_base = date.today()

    id = db.Column(db.Integer, primary_key=True)

    tipo = db.Column(db.String(20), nullable=False)

    modelo = db.Column(db.String(50), nullable=False)

    implementacao = db.Column(db.DateTime, default=data_base)

    def json(self):
        return {'tipo': self.tipo,
                'modelo': self.modelo,
                'implementacao': self.implementacao
               }