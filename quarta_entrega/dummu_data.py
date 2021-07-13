from app.extensions import db
from app.funcionarios.model import Funcionario
from app.maquinas.model import Maquina
from app.association import tabela_funcionario_maquina

def create_dd(app):
    with app.app_context():
        db.create_all()
        db.session.commit()


    pass