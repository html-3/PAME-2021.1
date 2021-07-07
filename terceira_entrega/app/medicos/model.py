from extensions import db

# id = chave primaria
# nome = nome completo: tamanho 30, obrigatoria, unica
# esp = especializacao: tamanho 15, obrigatoria
# cel = celular do medico: tamanho 15, default
# email = email do medico: tamanho 30, default

# contatos da clinica (placeholder)
# salvar em um lugar mais apropriado
tel_clinica = "(21) 99999-9999"
email_clinica = "clinica.marcus@gmail.com"

class Medicos(db.Model):

    # nome da tabela
    __tablename__ = "médicos"

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
    
    # consultas (one-to-many)
    consultas = db.relationship("Consulta", cascade="all, delete", backref="medicos", lazy=True)

    # impressao da classe
    def __repr__(self):
        return f"Médico: {self.nome} - {self.esp} - {self.email}"