from app.extensions import db
from app.funcionarios.model import Funcionario
from app.maquinas.model import Maquina
from app.association import tabela_funcionario_maquina
from datetime import datetime

def create_dd(app):
    with app.app_context():
        db.create_all()
        db.session.commit()

        if not Funcionario.query.first():
            pedro = Funcionario(nome="Pedro Rocha",
                                registro="pedro_rocha1",
                                senha="senha456")
            
            lais = Funcionario(nome="Lais Quintas",
                                registro="lais_quintas1",
                                cargo="Gerente")

            db.session.add(pedro)
            db.session.add(lais)
            db.session.commit()

        if not Maquina.query.first():
            maq1 = Maquina(modelo="Pesadora Aplha Mega 2.0",
                           implementacao=datetime(2020, 6, 1))
            
            maq2 = Maquina(modelo="Distribuidora Beta 3")

            maq3 = Maquina(modelo="Esteira Deluxe Premium",
                           implementacao=datetime(2021, 7, 1))

            db.session.add(maq1)
            db.session.add(maq2)
            db.session.add(maq3)
            db.session.commit()

            maq1.operadores.append(pedro)
            maq2.operadores.append(pedro)
            maq1.operadores.append(lais)

            db.session.commit()
               