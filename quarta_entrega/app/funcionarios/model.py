from app.extensions import db
from app.association import tabela_funcionario_maquina

class Funcionario(db.Model):

    senha_base = "password123"

    cargo_base = "Operador de Máquina"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(30), nullable=False)

    registro = db.Column(db.String(30), nullable=False, unique=True)

    senha = db.Column(db.String(30), default=senha_base)

    cargo = db.Column(db.String(30), default=cargo_base)


    maquinas = db.relationship("Maquina", secondary=tabela_funcionario_maquina, backref='operadores', lazy=True)