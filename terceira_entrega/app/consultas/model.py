from app.extensions import db

# id = chave primaria
# horario = hora e dia da consulta: (ano, mes, dia), obrigatoria, unica

# paciente_id = id do paciente:
# paciente = paciente (instancia):

# medico_id = id do medico:
# medico = medico (instancia):


class Consulta(db.Model):

    # nome da tabela
    __tablename__ = "consultas"

    # id de cada elemento da tabela
    id = db.Column(db.Integer, primary_key=True)

    # horario (usar outro tipo que nao seja string)
    horario = db.Column(db.DateTime(), nullable=False, unique=True)

    # paciente (one-to-one)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    # este nao aparece na db, apenas estabelece a relacao
    paciente = db.relationship("Paciente", cascade="all, delete", backref="consultas", lazy=True)

    # medico (one-to-one)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    # este nao aparece na db, apenas estabelece a relacao
    medico = db.relationship("Medico", cascade="all, delete", backref="consultas", lazy=True)


    # impressao da classe
    def __repr__(self):
        return f"Consulta: {self.horario} - {self.medico_id} - {self.paciente_id}"