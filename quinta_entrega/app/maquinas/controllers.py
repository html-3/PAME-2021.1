from flask import request
from flask.views import MethodView
from app.maquinas.utils import maquinas, maquina_utilidades
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.funcionarios.utils import adm_requerido

# aqui as autorizacoes sao avaliadas e as funcoes de cada metodo sao chamadas

class MaquinasGeral(MethodView): # /maquinas
    decorators = [jwt_required()]

    def get(self):
        id_usuario = get_jwt_identity()
        return maquinas(id_usuario)

    @adm_requerido
    def post(self):
        dados = request.json
        return maquina_utilidades(dados, 0, "POST")

class MaquinasParticular(MethodView): # /maquina/<int:id_escolhido>
    decorators = [jwt_required()]
    
    def get(self, id_escolhido):
        id_usuario = get_jwt_identity()
        return maquina_utilidades(0, id_escolhido, "GET", id_usuario)

    def patch(self, id_escolhido):
        id_usuario = get_jwt_identity()
        dados = request.json
        return maquina_utilidades(dados, id_escolhido, "PATCH", id_usuario)
    
    def delete(self, id_escolhido):
        id_usuario = get_jwt_identity()
        return maquina_utilidades(0, id_escolhido, "DELETE", id_usuario)
