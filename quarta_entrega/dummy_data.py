from app.extensions import db
from app.funcionarios.model import Funcionario
from app.maquinas.model import Maquina
from app.registros.model import Registro
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
            maq1 = Maquina(tipo="Pesadora",
                           modelo="Aplha Mega 2.0",
                           implementacao=datetime(2020, 6, 1))
            
            maq2 = Maquina(tipo="Distribuidora",
                           modelo="Beta 3")

            maq3 = Maquina(tipo="Esteira",
                           modelo="Deluxe Premium",
                           implementacao=datetime(2021, 7, 1))

            db.session.add(maq1)
            db.session.add(maq2)
            db.session.add(maq3)
            db.session.commit()

            maq1.operadores.append(pedro)
            maq2.operadores.append(pedro)
            maq1.operadores.append(lais)

        if not Registro.query.first():
            reg1 = Registro(horario=datetime(2020, 6, 1, 13),
                            temperatura=53.12,
                            peso_medio=20.34,
                            maquina=maq1)
            
            db.session.add(reg1)
            db.session.commit()

        db.session.commit()
               