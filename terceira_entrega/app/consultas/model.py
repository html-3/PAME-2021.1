from app.extensions import db

# id = chave primaria
# horario = hora e dia da consulta: (ano, mes, dia), obrigatoria, unica

# pacientes = pacientes (relacionamento):
# medicos = medicos (relacionamento):


class Consulta(db.Model):

    # nome da tabela
    #__tablename__ = "consultas"
    # estava causando problemas entao foi comentado

    # id de cada elemento da tabela
    id = db.Column(db.Integer, primary_key=True)

    # horario (usar outro tipo que nao seja string)
    horario = db.Column(db.DateTime(), nullable=False, unique=True)

    # paciente (one-to-many)
    # uma consulta pode ser de apenas um paciente
    # um paciente pode ter varias consultas
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))

    # medico (one-to-many)
    # uma consulta pode ser feita por apenas um medico
    # um medico pode ter varias consultas
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))



    # impressao da classe
    def __repr__(self):
        return f"Consulta: {self.horario} - {self.medico_id} - {self.paciente_id}"