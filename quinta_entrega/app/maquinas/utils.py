from app.funcionarios.model import Funcionario
from flask import jsonify
from app.extensions import db
from app.maquinas.model import Maquina
from datetime import datetime
from sqlalchemy import exc

# utilidades peso
def maquinas():
    maquinas = Maquina.query.all()

    return jsonify([maquina.json() for maquina in maquinas]), 200

def maquina_utilidades(dados, id_escolhido, metodo):
    if not isinstance(id_escolhido, int):
        return {'error': 'id_escolhido inválido'}, 400
        
    if metodo in ["GET", "PATCH", "DELETE"]:
        maquina = Maquina.query.get_or_404(id_escolhido)

    if metodo == "GET":
        return maquina.json(), 200

    if metodo == "DELETE":
        db.session.delete(maquina)
        db.session.commit()

        return maquina.json(), 200

    try:
        if metodo == "PATCH":
            tipo = dados.get('tipo', maquina.tipo)
            modelo = dados.get('modelo', maquina.modelo)
            implementacao = dados.get('implementacao', maquina.implementacao.strftime("%Y-%m-%d"))
            operadores = dados.get('operadores', maquina.operadores_base)

        elif metodo == "POST":
            tipo = dados.get('tipo')
            modelo = dados.get('modelo')
            implementacao = dados.get('implementacao', Maquina.data_base)
            operadores = dados.get('operadores', Maquina.operadores_base)

        if tipo == None or\
           modelo == None or\
           operadores == None:
            return {'error': 'faltou algum dado'}, 400

        tipo = str(tipo)[0:20]
        modelo = str(modelo)[0:20]
        implementacao = datetime.strptime(implementacao, "%Y-%m-%d")
        operadores = list(operadores)

        if metodo == "POST":
            maquina = Maquina(tipo=tipo,
                              modelo=modelo,
                              implementacao=implementacao)
            db.session.add(maquina)

        if metodo == "PATCH":
            maquina.tipo = tipo
            maquina.modelo = modelo
            maquina.implementacao = implementacao

        db.session.commit()

        if metodo == "PATCH" or metodo == "POST":
            for id_operador in operadores:
                operador = Funcionario.query.get_or_404(id_operador)
                maquina.operadores.append(operador)

        db.session.commit()

    #except TypeError:
    #    return {'error': 'operadores tem que ser uma lista'}, 400

    except ValueError:
        if not isinstance(implementacao, datetime):
            return {'error': 'implementacao no formato errado (YYYY-MM-DD)'}, 400

        return {'error': 'tipo inválido de modelo ou tipo'}, 400
        
    except exc.IntegrityError:
        db.session.rollback()
        return {'error': 'banco de dados comprometido'}, 400

    #except:
    #    return {'error': 'ocorreu um erro'}, 400

    return maquina.json(), 200