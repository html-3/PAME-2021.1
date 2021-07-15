from flask import request
from flask.views import MethodView
from app.maquinas.utils import maquinas, maquina_utilidades
from app.funcionarios.model import Funcionario
from flask_jwt_extended import jwt_required, get_jwt_identity

# aqui as autorizacoes sao avaliadas e as funcoes de cada metodo sao chamadas

class MaquinasGeral(MethodView): # /maquinas
    decorators = [jwt_required()]

    def get(self):
        id_usuario = get_jwt_identity()
        usuario = Funcionario.query.filter_by(id=id_usuario).first()
        if usuario.adm != True:
            return {'erro': 'acesso negado'}, 400
        return maquinas(id_usuario)


    def post(self):
        id_usuario = get_jwt_identity()
        usuario = Funcionario.query.filter_by(id=id_usuario).first()
        if usuario.adm != True:
            return {'erro': 'acesso negado'}, 400
        dados = request.json
        return maquina_utilidades(dados, 0, "POST")

class MaquinasParticular(MethodView): # /maquina/<int:id_escolhido>
    decorators = [jwt_required()]
    
    def get(self, id_escolhido):
        return maquina_utilidades(0, id_escolhido, "GET")

    def patch(self, id_escolhido):
        dados = request.json
        return maquina_utilidades(dados, id_escolhido, "PATCH")
    
    def delete(self, id_escolhido):
        return maquina_utilidades(0, id_escolhido, "DELETE")
