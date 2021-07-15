from app.extensions import db

# Registro: 
# - id: chave principal
# - horario: horario do registro (cada 1 min), obrigatoria
# - temp1: temperatura do motor 1, obrigatoria
# - temp2: temperatura do motor 2, obrigatoria
# - temp3: temperatura do motor 3, obrigatoria
# - temp4: temperatura do motor 4, obrigatoria
# - temp5: temperatura do motor 5, obrigatoria

# Peso: 
# - id: chave principal
# - bolsa_id: id da bolsa (XXXXXXDDMMYY), obrigatoria, unica
# - peso: peso da bolsa, obrigatoria
# - maquina_id: maquina que fez o registro, externa

class Temperatura(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    horario = db.Column(db.DateTime, nullable=False)

    temp1 = db.Column(db.Float, nullable=False)

    temp2 = db.Column(db.Float, nullable=False)

    temp3 = db.Column(db.Float, nullable=False)

    temp4 = db.Column(db.Float, nullable=False)

    temp5 = db.Column(db.Float, nullable=False)

    def json(self):
        return {'horario': self.horario.strftime("%Y-%m-%d %H:%M:%S"),
                'temp1': self.temp1,
                'temp2': self.temp2,
                'temp3': self.temp3,
                'temp4': self.temp4,
                'temp5': self.temp5
               }

class Peso(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    bolsa_id = db.Column(db.String(12), nullable=False, unique=True)

    peso_kg = db.Column(db.Float, nullable=False)

    maquina_id = db.Column(db.Integer, db.ForeignKey('maquina.id'))

    def json(self):
        return {'bolsa_id': self.bolsa_id,
                'peso_kg': self.peso_kg,
                'maquina_id': self.maquina_id
               }