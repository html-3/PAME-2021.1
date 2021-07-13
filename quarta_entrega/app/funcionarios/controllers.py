from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import exc
from app.extensions import db
from app.funcionarios.model import Funcionario

class FuncionariosGeral(MethodView): # /funcionarios

    def get(self):
        funcionarios = Funcionario.query.all()
        
        return jsonify([funcionario.json() for funcionario in funcionarios]), 200


    def post(self):
        if True:
            dados = request.json

            try:
                nome = str(dados.get('nome'))[0:30]
                registro = str(dados.get('registro'))[0:30]
                senha = str(dados.get('senha', Funcionario.senha_base))[0:30]
                cargo = str(dados.get('cargo', Funcionario.cargo_base))[0:30]

                # evita que dados incompletos sejam enviados
                if nome == "None" or registro == "None":
                    return {'error': 'faltou algum dado'}, 400

                funcionario = Funcionario(nome=nome,
                                      registro=registro,
                                      senha=senha,
                                      cargo=cargo)

                db.session.add(funcionario)
                db.session.commit()

            # com a funcao str(), obriga o input ser uma string, ou convertivel para uma string
            except ValueError:
                return {'error': 'tipo invalido'}, 400

            # o registro do funcionario deve ser unico
            except exc.IntegrityError:
                db.session.rollback()
                return {'error': 'registro deve ser unico'}, 400

            # pegar oustros erros quaisquer (nunca disparou mas nunca se sabe)
            except:
                return {'error': 'ocorreu um erro'}, 400
            
        return funcionario.json(), 200

class FuncionariosParcicular(MethodView): # /funcionario/<int:id_escolhido>
    
    def get(self, id_escolhido):
        funcionario = Funcionario.query.get_or_404(id_escolhido)

        return funcionario.json(), 200


    def put(self, id_escolhido):
        funcionario = Funcionario.query.get_or_404(id_escolhido)
        dados = request.json

        try:
            nome = str(dados.get('nome'))[0:30]
            registro = str(dados.get('registro'))[0:30]
            senha = str(dados.get('senha'))[0:30]
            cargo = str(dados.get('cargo'))[0:30]

            # evita que dados incompletos sejam enviados
            if nome == "None" or registro == "None" or senha == "None" or cargo == "None":
                    return {'error': 'faltou algum dado'}, 400

            funcionario.nome = nome
            funcionario.registro = registro
            funcionario.senha = senha
            funcionario.cargo = cargo

            db.session.commit()

        # com a funcao str(), obriga o input ser uma string, ou convertivel para uma string
        except ValueError:
            return {'error': 'tipo invalido'}, 400

        # o registro do funcionario deve ser unico
        except exc.IntegrityError:
            db.session.rollback()
            return {'error': 'registro deve ser unico'}, 400

        # pegar oustros erros quaisquer (nunca disparou mas nunca se sabe)
        except:
            return {'error': 'ocorreu um erro'}, 400
        
        return funcionario.json(), 200


    def patch(self, id_escolhido):
        funcionario = Funcionario.query.get_or_404(id_escolhido)
        dados = request.json

        try:
            nome = str(dados.get('nome', funcionario.nome))[0:30]
            registro = str(dados.get('registro', funcionario.registro))[0:30]
            senha = str(dados.get('senha', funcionario.senha))[0:30]
            cargo = str(dados.get('cargo', funcionario.cargo))[0:30]

            funcionario.nome = nome
            funcionario.registro = registro
            funcionario.senha = senha
            funcionario.cargo = cargo

            db.session.commit()

        # com a funcao str(), obriga o input ser uma string, ou convertivel para uma string
        except ValueError:
            return {'error': 'tipo invalido'}, 400

        # o registro do funcionario deve ser unico
        except exc.IntegrityError:
            db.session.rollback()
            return {'error': 'registro deve ser unico'}, 400

        # pegar oustros erros quaisquer (nunca disparou mas nunca se sabe)
        except:
            return {'error': 'ocorreu um erro'}, 400
        
        return funcionario.json(), 200
    

    def delete(self, id_escolhido):
        funcionario = Funcionario.query.get_or_404(id_escolhido)

        db.session.delete(funcionario)
        db.session.commit()

        return funcionario.json(), 200
