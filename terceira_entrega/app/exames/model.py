from app.extensions import db

# id = chave primaria
# horario = hora e dia da consulta: (ano, mes, dia), obrigatoria, unica

# paciente_id = id do paciente:
# paciente = paciente (instancia):

# medico_id = id do medico:
# medico = medico (instancia):


class Exame(db.Model):

    # nome da tabela
    #__tablename__ = "exames"

    # id de cada elemento da tabela
    id = db.Column(db.Integer, primary_key=True)

    # horario (usar outro tipo que nao seja string)
    horario = db.Column(db.DateTime, nullable=False, unique=True)

    # tipo de exame
    tipo = db.Column(db.String(30), nullable=False)

    # examens medicos (one-to-many)
    # um exame pode ser de apenas um paciente
    # um paciente pode ter varios exames
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))

    # impressao da classe
    def __repr__(self):
        return f"Exame: {self.horario} - {self.tipo} - {self.paciente_id}"