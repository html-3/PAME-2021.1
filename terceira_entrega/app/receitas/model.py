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
    #__tablename__ = "receitas"

    # id de cada elemento da tabela
    id = db.Column(db.Integer, primary_key=True)

    # data de expedicao
    data = db.Column(db.DateTime, default=date.today)

    # conteudo
    cont = db.Column(db.String(300), nullable=False)

    # paciente (one-to-many)
    # uma receita pode ser de apenas um paciente
    # um paciente pode ter varias receitas
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))

    # medico (one-to-one)
    # uma receita pode ser prescrita por apenas um medico
    # um medico pode prescrever varias receitas
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))

    # impressao da classe
    def __repr__(self):
        return f"Receita: {self.data} - {self.paciente_id} - {self.medico_id}"