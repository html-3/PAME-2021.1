from app.extensions import db

# id = chave primaria
# nome = nome completo: tamanho 30, obrigatoria
# cpf = identificacao: tamanho 14, obrigatoria, unica
# cel = celular do medico: tamanho 15, obrigatoria, unica
# email = email do medico: tamanho 30, obrigatoria, unica
# plano_saude = plano de saude: tamanho 40, obrigatoria

# receitas = receitas (relacionamento):

class Paciente(db.Model):

    # nome da tabela
    #__tablename__ = "pacientes"

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

    # prescricoes (one-to-many)
    # uma receita pode ter apenas um paciente
    # um paciente pode ter varias receitas
    receitas = db.relationship("Receita", backref='paciente', lazy=True)

    # consultas (one-to-many)
    # uma consulta pode ser de apenas um paciente
    # um paciente pode ter varias consultas
    consultas = db.relationship("Consulta", backref='paciente', lazy=True)

    # examens medicos (one-to-many)
    # um exame pode ser de apenas um paciente
    # um paciente pode ter varios exames
    exames = db.relationship("Exame", backref='paciente', lazy=True)

    # impressao da classe
    def __repr__(self):
        return f"Paciente: {self.nome} - {self.cpf} - {self.plano_saude}"