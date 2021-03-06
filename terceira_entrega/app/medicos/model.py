from app.extensions import db

# id = chave primaria
# nome = nome completo: tamanho 30, obrigatoria, unica
# esp = especializacao: tamanho 15, obrigatoria
# cel = celular do medico: tamanho 15, default
# email = email do medico: tamanho 30, default

# receitas = receitas (relacionamento):
# consultas = receitas (relacionamento):

class Medico(db.Model):

    # nome da tabela
    #__tablename__ = "médicos"
    # estava causando problemas entao foi comentado

    # contatos da clinica (placeholder)
    # salvar em um lugar mais apropriado
    tel_clinica = "(21) 99999-9999"
    email_clinica = "clinica.marcus@gmail.com"

    # id de cada elemento da tabela
    id = db.Column(db.Integer, primary_key=True)

    # nome dos medicos
    nome = db.Column(db.String(30), nullable=False, unique=True)

    # especializacao
    # obstetra, ginecologista e pediatra.
    esp = db.Column(db.String(15), nullable=False)

    # contato (numero)
    cel = db.Column(db.String(15), default=tel_clinica)

    # contato (email)
    email = db.Column(db.String(30), default=email_clinica)
    
    # medico (one-to-many)
    # uma receita pode ser prescrita por apenas um medico
    # um medico pode prescrever varias receitas
    receitas = db.relationship("Receita", backref='medico', lazy=True)

    # medico (one-to-many)
    # uma consulta pode ser feita por apenas um medico
    # um medico pode ter varias consultas    
    consultas = db.relationship("Consulta", backref='medico', lazy=True)

    # impressao da classe
    def __repr__(self):
        return f"Médico: {self.nome} - {self.esp} - {self.email}"