from app.extensions import db

# id = chave primaria
# nome = nome completo: tamanho 30, obrigatoria
# cpf = identificacao: tamanho 14, obrigatoria, unica
# cel = celular do medico: tamanho 15, obrigatoria, unica
# email = email do medico: tamanho 30, obrigatoria, unica
# plano_saude = plano de saude: tamanho 40, obrigatoria

# receita_id = id da receita:
# receita = receita (instancia):

class Paciente(db.Model):

    # nome da tabela
    __tablename__ = "pacientes"

    # id de cada elemento da tabela
    id = db.Column(db.Integer, primary_key=True)

    # nome dos medicos
    nome = db.Column(db.String(30), nullable=False)

    # cadastro de pessoa fisica
    cpf = db.Column(db.String(14), nullable=False, unique=True)

    # contato (numero)
    cel = db.Column(db.String(15), nullable=False)

    # contato (email)
    email = db.Column(db.String(30), nullable=False)
    
    # nome e tipo do plano de saude
    plano_saude = db.Column(db.String(40), nullable=False)

    # prescricoes (many-to-one)
    receita_id = db.Column(db.Integer, db.ForeignKey('receita.id'))
    # este nao aparece na db, apenas estabelece a relacao
    receita = db.relationship("Receita", cascade="all, delete", backref="pacientes", lazy=True)

    # impressao da classe
    def __repr__(self):
        return f"Paciente: {self.nome} - {self.cpf} - {self.plano_saude}"