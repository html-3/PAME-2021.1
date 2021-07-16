from flask import request
from flask.views import MethodView
from app.funcionarios.model import Funcionario
from app.funcionarios.utils import funcionarios, funcionario_utilidades, login, adm_requerido
from flask_jwt_extended import jwt_required, get_jwt_identity

# aqui as autorizacoes sao avaliadas e as funcoes de cada metodo sao chamadas

class FuncionariosLogin(MethodView): # /login

    def post(self):
        dados = request.json
        return login(dados)

class FuncionariosGeral(MethodView): # /funcionarios
    decorators = [jwt_required()]
    
    @adm_requerido
    def get(self):
        return funcionarios()

    @adm_requerido
    def post(self):
        dados = request.json
        return funcionario_utilidades(dados, 0, "POST")

class FuncionariosParcicular(MethodView): # /funcionario/<int:id_escolhido>
    decorators = [jwt_required()]

    def get(self, id_escolhido):
        id_usuario = get_jwt_identity()
        usuario = Funcionario.query.filter_by(id=id_usuario).first()
        if get_jwt_identity() != id_escolhido or usuario.adm != True:
            return {'erro': 'acesso negado'}, 400

        return funcionario_utilidades(0, id_escolhido, "GET")

    def patch(self, id_escolhido):
        id_usuario = get_jwt_identity()
        usuario = Funcionario.query.filter_by(id=id_usuario).first()
        if get_jwt_identity() != id_escolhido or usuario.adm != True:
            return {'erro': 'acesso negado'}, 400

        dados = request.json
        return funcionario_utilidades(dados, id_escolhido, "PATCH")
    

    def delete(self, id_escolhido):
        id_usuario = get_jwt_identity()
        usuario = Funcionario.query.filter_by(id=id_usuario).first()
        if get_jwt_identity() != id_escolhido or usuario.adm != True:
            return {'erro': 'acesso negado'}, 400

        return funcionario_utilidades(0, id_escolhido, "DELETE")
