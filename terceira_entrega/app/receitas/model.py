from datetime import date
from app.extensions import db

# id = chave primaria
# data = data de expedicao: default
# cont = conteudo da receita: tamanho 300, obrigatoria

# paciente_id = id do paciente:
# paciente = paciente (instancia):

# medico_id = id do medico:
# medico = medico (instancia):

class Receita(db.Model):

    # nome da tabela
    __tablename__ = "receitas"

    # id de cada elemento da tabela
    id = db.Column(db.Integer, primary_key=True)

    # data de expedicao
    data = db.Column(db.DateTime, default=date.today)

    # conteudo
    cont = db.Column(db.String(300), nullable=False)

    # paciente (one-to-one)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    # este nao aparece na db, apenas estabelece a relacao
    paciente = db.relationship("Paciente", cascade="all, delete", backref="receitas", lazy=True)

    # medico (one-to-one)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    # este nao aparece na db, apenas estabelece a relacao
    medico = db.relationship("Medico", cascade="all, delete", backref="receitas", lazy=True)

    # impressao da classe
    def __repr__(self):
        return f"Receita: {self.data} - {self.paciente_id} - {self.medico_id}"