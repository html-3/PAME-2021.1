from app.extensions import db
from app.association import tabela_funcionario_maquina
import bcrypt

# Funcionario: 
# - id: chave principal
# - nome: nome do funcionario, obrigatoria
# - email: nome de usuario, obrigatoria, unica
# - senha, default
# - cargo: papel na empresa, default
# - adm: poderes de administrador ou moderacao, default


class Funcionario(db.Model):

    senha_base = "password123"
    senha_base_hash = bcrypt.hashpw("password123".encode(), bcrypt.gensalt())
    cargo_base = "Operador de Máquina"
    adm_base = False

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(30), nullable=False)

    email = db.Column(db.String(30), nullable=False, unique=True)

    senha_hash = db.Column(db.String(100), default=senha_base_hash)

    cargo = db.Column(db.String(30), default=cargo_base)

    adm = db.Column(db.Boolean, default=adm_base)

    maquinas = db.relationship("Maquina", secondary=tabela_funcionario_maquina, backref='operadores', lazy=True)

    def json(self):
        return {'nome': self.nome,
                'email': self.email,
                'cargo': self.cargo
               }