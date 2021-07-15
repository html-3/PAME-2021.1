from flask import request
from flask.views import MethodView
from app.funcionarios.model import Funcionario
from app.funcionarios.utils import funcionarios, funcionario_utilidades, login
from flask_jwt_extended import jwt_required, get_jwt_identity

class FuncionariosLogin(MethodView): # /login

    def post(self):
        dados = request.json
        return login(dados)

class FuncionariosGeral(MethodView): # /funcionarios
    decorators = [jwt_required()]
    
    def get(self):
        usuario = Funcionario.query.filter_by(id=get_jwt_identity()).first()
        if usuario.adm != True:
            return {'erro': 'acesso negado'}, 400

        else:
            return funcionarios()

    def post(self):
        usuario = Funcionario.query.filter_by(id=get_jwt_identity()).first()
        if usuario.adm != True:
            return {'erro': 'acesso negado'}, 400

        else:
            dados = request.json
            return funcionario_utilidades(dados, 0, "POST")

class FuncionariosParcicular(MethodView): # /funcionario/<int:id_escolhido>
    decorators = [jwt_required()]

    def get(self, id_escolhido):
        usuario = Funcionario.query.filter_by(id=get_jwt_identity()).first()
        if get_jwt_identity() != id_escolhido or usuario.adm != True:
            return {'erro': 'acesso negado'}, 400

        return funcionario_utilidades(0, id_escolhido, "GET")

    def patch(self, id_escolhido):
        usuario = Funcionario.query.filter_by(id=get_jwt_identity()).first()
        if get_jwt_identity() != id_escolhido or usuario.adm != True:
            return {'erro': 'acesso negado'}, 400

        dados = request.json
        return funcionario_utilidades(dados, id_escolhido, "PATCH")
    

    def delete(self, id_escolhido):
        usuario = Funcionario.query.filter_by(id=get_jwt_identity()).first()
        if get_jwt_identity() != id_escolhido or usuario.adm != True:
            return {'erro': 'acesso negado'}, 400

        return funcionario_utilidades(0, id_escolhido, "DELETE")
