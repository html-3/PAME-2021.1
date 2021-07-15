from flask import jsonify
from app.maquinas.model import Maquina
from app.extensions import db
from app.registros.model import Temperatura, Peso
from datetime import datetime
from sqlalchemy import exc

# utilidades temperatura
def temperaturas():
    temperaturas = Temperatura.query.all()

    return jsonify([temperatura.json() for temperatura in temperaturas]), 200

def temperatura_utilidades(dados, id_escolhido, metodo):
    if not isinstance(id_escolhido, int):
        return {'error': 'id_escolhido inválido'}, 400
        
    if metodo in ["GET", "PATCH", "DELETE"]:
        temperatura = Temperatura.query.get_or_404(id_escolhido)

    if metodo == "GET":
        return temperatura.json(), 200

    if metodo == "DELETE":
        db.session.delete(temperatura)
        db.session.commit()

        return temperatura.json(), 200

    try:
        if metodo == "PATCH":
            horario = dados.get('horario', temperatura.horario)
            temp1 = dados.get('temp1', temperatura.temp1)
            temp2 = dados.get('temp2', temperatura.temp2)
            temp3 = dados.get('temp3', temperatura.temp3)
            temp4 = dados.get('temp4', temperatura.temp4)
            temp5 = dados.get('temp5', temperatura.temp5)

        elif metodo == "POST":
            horario = dados.get('horario')
            temp1 = dados.get('temp1')
            temp2 = dados.get('temp2')
            temp3 = dados.get('temp3')
            temp4 = dados.get('temp4')
            temp5 = dados.get('temp5')

        if temp1 == None or\
           temp2 == None or\
           temp3 == None or\
           temp4 == None or\
           temp5 == None:
            return {'error': 'faltou algum dado'}, 400

        horario =  datetime.strptime(horario, "%Y-%m-%d %H:%M:%S")
        temp1 = round(float(temp1), 2)
        temp2 = round(float(temp2), 2)
        temp3 = round(float(temp3), 2)
        temp4 = round(float(temp4), 2)
        temp5 = round(float(temp5), 2)

        if metodo == "POST":
            temperatura = Temperatura(horario=horario,
                                      temp1=temp1,
                                      temp2=temp2,
                                      temp3=temp3,
                                      temp4=temp4,
                                      temp5=temp5)
            db.session.add(temperatura)

        if metodo == "PATCH":
            temperatura.horario = horario
            temperatura.temp1 = temp1
            temperatura.temp2 = temp2
            temperatura.temp3 = temp3
            temperatura.temp4 = temp4
            temperatura.temp5 = temp5

        db.session.commit()

    except ValueError:
        if not isinstance(temp1 , float) or\
           not isinstance(temp2 , float) or\
           not isinstance(temp3 , float) or\
           not isinstance(temp4 , float) or\
           not isinstance(temp5 , float):
            return {'error': 'temperatura não é float'}, 400
        
        else:
            return {'error': 'horário no formato errado (YYYY-MM-DD HH:MM:SS)'}, 400

    except exc.IntegrityError:
        db.session.rollback()
        return {'error': 'integridade do banco de dados comprometida'}, 400

    except:
        return {'error': 'ocorreu um erro'}, 400

    return temperatura.json(), 200

# utilidades peso
def pesos():
    pesos = Peso.query.all()

    return jsonify([peso.json() for peso in pesos]), 200

def peso_utilidades(dados, id_escolhido, metodo):
    if not isinstance(id_escolhido, int):
        return {'error': 'id_escolhido inválido'}, 400
        
    if metodo in ["GET", "PATCH", "DELETE"]:
        peso = Peso.query.get_or_404(id_escolhido)

    if metodo == "GET":
        return peso.json(), 200

    if metodo == "DELETE":
        db.session.delete(peso)
        db.session.commit()
        
        return peso.json(), 200

    try:
        if metodo == "PATCH":
            bolsa_id = dados.get('bolsa_id', peso.bolsa_id)
            peso_kg = dados.get('peso_kg', peso.peso_kg)
            maquina_id = dados.get('maquina_id', peso.maquina_id)

        elif metodo == "POST":
            bolsa_id = dados.get('bolsa_id')
            peso_kg = dados.get('peso_kg')
            maquina_id = dados.get('maquina_id')

        if bolsa_id == None or\
           peso_kg == None or\
           maquina_id == None:
            return {'error': 'faltou algum dado'}, 400

        bolsa_id = str(bolsa_id)[0:12]
        peso_kg = round(float(peso_kg), 2)
        maquina_id = int(maquina_id)

        if len(bolsa_id) < 12:
            return {'error': 'tipo inválido de bolsa_id'}

        if metodo == "POST":
            maquina = Maquina.query.get_or_404(maquina_id)

            peso = Peso(bolsa_id=bolsa_id,
                        peso_kg=peso_kg,
                        maquina=maquina)
            db.session.add(peso)

        if metodo == "PATCH":
            maquina = Maquina.query.get_or_404(maquina_id)

            peso.bolsa_id = bolsa_id
            peso.peso_kg = peso_kg
            peso.maquina = maquina

        db.session.commit()

    except ValueError:
        """
        if not isinstance(bolsa_id , int) or\
           not isinstance(peso_kg, float) or\
           not isinstance(maquina_id, int):
        """

        return {'error': 'tipo inválido de bolsa_id, peso_kg ou maquina_id'}, 400

    except exc.IntegrityError:
        db.session.rollback()
        return {'error': 'bolsa_id inválido'}, 400


    """
    except:
        return {'error': 'ocorreu um erro'}, 400"""

    return peso.json(), 200