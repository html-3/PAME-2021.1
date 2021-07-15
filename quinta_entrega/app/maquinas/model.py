from app.extensions import db
from datetime import date

# Maquina: 
# - id: chave principal
# - tipo: funcao/tipo de maquina, default
# - modelo: variante ou versao da maquina, obrigatoria
# - implementacao: data do comeco de uso (questoes de manutencao periodica), default

class Maquina(db.Model):

    data_base = date.today()

    tipo_base = "Motor Esteira"

    operadores_base = []

    id = db.Column(db.Integer, primary_key=True)

    tipo = db.Column(db.String(20), default=data_base)

    modelo = db.Column(db.String(20), nullable=False)

    implementacao = db.Column(db.DateTime, default=data_base)

    pesos_medidos = db.relationship("Peso", backref='maquina', lazy=True)

    def json(self):
        return {'tipo': self.tipo,
                'modelo': self.modelo,
                'implementacao': self.implementacao.strftime("%Y-%m-%d")
               }