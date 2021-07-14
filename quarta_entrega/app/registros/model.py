from enum import unique
from app.extensions import db
from datetime import date

# Registro: 
# - id: chave principal
# - horario: horario do registro
# - temperatura: temperatura da maquina, obrigatoria
# - peso_medio: peso medio de cada saca de farinha, obrigatoria
# - maquina_id: id da maquina que vez o registro, externa

class Registro(db.Model):

    data_base = date.today()

    id = db.Column(db.Integer, primary_key=True)

    horario = db.Column(db.DateTime, nullable=False)

    temperatura = db.Column(db.Float(2), nullable=False)

    peso_medio = db.Column(db.Float(2), nullable=False)

    maquina_id = db.Column(db.Integer, db.ForeignKey('maquina.id'))

    def json(self):
        return {'horario': self.horario,
                'temperatura': self.temperatura,
                'peso_medio': self.peso_medio
               }