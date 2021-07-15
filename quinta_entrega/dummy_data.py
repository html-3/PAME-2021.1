from app.extensions import db
from app.funcionarios.model import Funcionario
from app.maquinas.model import Maquina
from app.registros.model import Temperatura, Peso
from app.association import tabela_funcionario_maquina
from datetime import datetime

def create_dd(app):
    with app.app_context():
        db.create_all()
        db.session.commit()

        if not Funcionario.query.first():
            pedro = Funcionario(nome="Pedro Rocha",
                                registro="pedro.rocha1980@gmail.com",
                                senha="senha456")
            
            will = Funcionario(nome="William Carvalho",
                                registro="william.carvalho@gmail.com",
                                cargo="Estagiário")
            
            lais = Funcionario(nome="Lais Quintas",
                                registro="lais.quintas1@gmail.com",
                                cargo="Gerente",
                                senha="senha789")

            db.session.add(pedro)
            db.session.add(lais)
            db.session.add(will)
            db.session.commit()

        if not Maquina.query.first():
            maq1 = Maquina(tipo="Motor de Esteira",
                           modelo="Mega",
                           implementacao=datetime(2020, 9, 1))
            
            maq2 = Maquina(tipo="Motor de Esteira",
                           modelo="Beta 3")

            maq3 = Maquina(tipo="Motor de Esteira",
                           modelo="Deluxe Premium",
                           implementacao=datetime(2021, 2, 1))
            
            maq4 = Maquina(tipo="Motor de Esteira",
                           modelo="Deluxe Premium",
                           implementacao=datetime(2021, 2, 1))
            
            maq5 = Maquina(tipo="Motor de Esteira",
                           modelo="Deluxe Premium 2",
                           implementacao=datetime(2021, 6, 1))

            db.session.add(maq1)
            db.session.add(maq2)
            db.session.add(maq3)
            db.session.add(maq4)
            db.session.add(maq5)
            db.session.commit()

            maq1.operadores.append(will)
            maq1.operadores.append(pedro)
            maq2.operadores.append(pedro)
            maq3.operadores.append(pedro)
            maq4.operadores.append(pedro)
            maq5.operadores.append(pedro)
            maq3.operadores.append(lais)
            maq4.operadores.append(lais)
            maq5.operadores.append(lais)
            db.session.commit()

        if not Temperatura.query.first():
            db.session.add(Temperatura(horario=datetime(2020, 6, 1, 8, 00, 00),
                                       temp1=50.50,
                                       temp2=51.25,
                                       temp3=50.81,
                                       temp4=49.25,
                                       temp5=50.50))
            db.session.add(Temperatura(horario=datetime(2020, 6, 1, 9, 00, 00),
                                       temp1=77.50,
                                       temp2=68.25,
                                       temp3=75.81,
                                       temp4=80.25,
                                       temp5=64.50))
            db.session.add(Temperatura(horario=datetime(2020, 6, 1, 9, 1, 00),
                                       temp1=76.50,
                                       temp2=70.25,
                                       temp3=76.75,
                                       temp4=79.25,
                                       temp5=62.50))

            db.session.commit()
            
        if not Peso.query.first():
            db.session.add(Peso(bolsa_id="000000140721",
                                peso_kg=20.20,
                                maquina=maq1))
            db.session.add(Peso(bolsa_id="000001140721",
                                peso_kg=20.00,
                                maquina=maq2))
            db.session.add(Peso(bolsa_id="000002140721",
                                peso_kg=19.90,
                                maquina=maq3))
            db.session.add(Peso(bolsa_id="00000A140721",
                                peso_kg=20.05,
                                maquina=maq4))
            db.session.add(Peso(bolsa_id="00000B140721",
                                peso_kg=21.00,
                                maquina=maq5))
            db.session.add(Peso(bolsa_id="000003140721",
                                peso_kg=20.05,
                                maquina=maq5))
            
            db.session.commit()

        db.session.commit()
               