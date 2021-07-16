from app.funcionarios.model import Funcionario
from flask import jsonify
from app.extensions import db
from app.maquinas.model import Maquina
from datetime import datetime
from sqlalchemy import exc
from app.association import tabela_funcionario_maquina

# aqui as funcionalidades dos metodos e outras funcoes sao definidas
# tambem sao feitos os testes de validacao dos dados, para enviar os erros ao front

# funcao para listar todas as maquinas
def maquinas(id_usuario):
    maquinas = Funcionario.query.get_or_404(id_usuario).maquinas
    return jsonify([maquina.json() for maquina in maquinas]), 200

# funcao composta para ver, adicionar, editar e deletar maquinas
def maquina_utilidades(dados, id_escolhido, metodo, id_usuario):
    if not isinstance(id_escolhido, int):
        return {'error': 'id_escolhido inválido'}, 400
    
    # defina a maquina a ser vista, editada ou deletada 
    # alem de conferir que ela seja operada pelo usuario
    if metodo in ["GET", "PATCH", "DELETE"]:
        maquinas = Funcionario.query.get_or_404(id_usuario).maquinas
        maquina = Maquina.query.get_or_404(id_escolhido)

        if not maquina in maquinas:
            return {'error': 'acesso negado à maquina'}, 400

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

    except TypeError:
        return {'error': 'operadores tem que ser uma lista'}, 400

    except ValueError:
        if not isinstance(implementacao, datetime):
            return {'error': 'implementacao no formato errado (YYYY-MM-DD)'}, 400

        return {'error': 'tipo inválido de modelo ou tipo'}, 400
        
    except exc.IntegrityError:
        db.session.rollback()
        return {'error': 'banco de dados comprometido'}, 400

    except:
        return {'error': 'ocorreu um erro'}, 400

    return maquina.json(), 200