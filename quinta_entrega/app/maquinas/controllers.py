from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import exc
from app.extensions import db
from app.maquinas.model import Maquina
from app.funcionarios.model import Funcionario
from datetime import date, datetime

class MaquinasGeral(MethodView): # /maquinas

    def get(self):
        maquinas = Maquina.query.all()
        
        return jsonify([maquina.json() for maquina in maquinas]), 200


    def post(self):
        if True:
            dados = request.json

            today_string = date.today().strftime("%Y-%m-%d")

            try:
                tipo = str(dados.get('tipo'))[0:20]
                modelo = str(dados.get('modelo'))[0:50]
                implementacao = datetime.strptime(dados.get('implementacao', today_string), "%Y-%m-%d")

                # evita que dados incompletos sejam enviados
                if tipo == "None" or modelo == "None":
                    return {'error': 'faltou algum dado'}, 400

                maquina = Maquina(tipo=tipo,
                                  modelo=modelo,
                                  implementacao=implementacao)

                db.session.add(maquina)
                db.session.commit()

            # com a funcao str(), obriga o input ser uma string, ou convertivel para uma string
            except ValueError:
                return {'error': 'tipo invalido (data deve ser YYYY-MM-DD)'}, 400
        
            # erros quaisquer do sqlalchemy
            except exc.IntegrityError:
                db.session.rollback()
                return {'error': 'integridade do banco de dados comprometida'}, 400

            # pegar oustros erros quaisquer (nunca disparou mas nunca se sabe)
            except:
                return {'error': 'ocorreu um erro'}, 400
            
        return maquina.json(), 200

class MaquinasParticular(MethodView): # /maquina/<int:id_escolhido>
    
    def get(self, id_escolhido):
        maquina = Maquina.query.get_or_404(id_escolhido)

        return maquina.json(), 200


    def put(self, id_escolhido):
        maquina = Maquina.query.get_or_404(id_escolhido)
        dados = request.json

        try:
            tipo = str(dados.get('tipo'))[0:20]
            modelo = str(dados.get('modelo'))[0:50]
            implementacao = datetime.strptime(dados.get('implementacao'),"%Y-%m-%d")

            # evita que dados incompletos sejam enviados
            if tipo == "None" or modelo == "None":
                return {'error': 'faltou algum dado'}, 400

            maquina.tipo = tipo
            maquina.modelo = modelo
            maquina.implementacao = implementacao

            db.session.commit()

        # com a funcao str(), obriga o input ser uma string, ou convertivel para uma string
        except ValueError:
            return {'error': 'tipo invalido'}, 400

        except TypeError:
            return {'error': 'falta data de implementacao da maquina'}, 400

        # erros quaisquer do sqlalchemy
        except exc.IntegrityError:
            db.session.rollback()
            return {'error': 'integridade do banco de dados comprometida'}, 400

        # pegar oustros erros quaisquer (nunca disparou mas nunca se sabe)
        except:
            return {'error': 'ocorreu um erro'}, 400
    
        return maquina.json(), 200


    def patch(self, id_escolhido):
        maquina = Maquina.query.get_or_404(id_escolhido)
        dados = request.json

        try:
            implementacao_previa = maquina.implementacao.strftime("%Y-%m-%d")

            tipo = str(dados.get('tipo', maquina.tipo))[0:20]
            modelo = str(dados.get('modelo', maquina.modelo))[0:50]
            implementacao = datetime.strptime(dados.get('implementacao', implementacao_previa), "%Y-%m-%d")

            # evita que dados incompletos sejam enviados
            if tipo == "None" or modelo == "None":
                return {'error': 'faltou algum dado'}, 400

            maquina.tipo = tipo
            maquina.modelo = modelo
            maquina.implementacao = implementacao

            db.session.commit()

        # com a funcao str(), obriga o input ser uma string, ou convertivel para uma string
        except ValueError:
            return {'error': 'tipo invalido (data deve ser YYYY-MM-DD)'}, 400

        # erros quaisquer do sqlalchemy
        except exc.IntegrityError:
            db.session.rollback()
            return {'error': 'integridade do banco de dados comprometida'}, 400

        # pegar oustros erros quaisquer (nunca disparou mas nunca se sabe)
        except:
            return {'error': 'ocorreu um erro'}, 400
        
        return maquina.json(), 200
    

    def delete(self, id_escolhido):
        maquina = Maquina.query.get_or_404(id_escolhido)

        db.session.delete(maquina)
        db.session.commit()

        return maquina.json(), 200

class MaquinasOperadores(MethodView): # /maquina/<int:id_maquina>/operadores
    
    def get(self, id_maquina):
        operadores = Maquina.query.get_or_404(id_maquina).operadores
        return jsonify([operador.json() for operador in operadores]), 200


    def post(self, id_maquina):
        maquina = Maquina.query.get_or_404(id_maquina)

        dados = request.json

        id_operador = dados.get('id_operador')

        if not id_operador or not isinstance(id_operador, int):
            return {'error': 'id_operador nao foi declarado ou invalido'}, 400

        operador = Funcionario.query.get_or_404(id_operador)

        maquina.operadores.append(operador)

        db.session.commit()

        operadores = Maquina.query.get_or_404(id_maquina).operadores
        return jsonify([operador.json() for operador in operadores]), 200
    

    def delete(self, id_maquina):
        maquina = Maquina.query.get_or_404(id_maquina)

        dados = request.json

        id_operador = dados.get('id_operador')

        if not id_operador or not isinstance(id_operador, int):
            return {'error': 'id_operador nao foi declarado ou invalido'}, 400

        operador = Funcionario.query.get_or_404(id_operador)
        try:
            maquina.operadores.remove(operador)

        except ValueError:
            return {'error': 'operador nao opera maquina'}, 400

        db.session.commit()

        operadores = Maquina.query.get_or_404(id_maquina).operadores
        return jsonify([operador.json() for operador in operadores]), 200