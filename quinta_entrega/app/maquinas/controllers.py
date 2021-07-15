from flask import request
from flask.views import MethodView
from app.maquinas.utils import maquinas, maquina_utilidades
from flask_jwt_extended import jwt_required, get_jwt_identity

class MaquinasGeral(MethodView): # /maquinas
    decorators = [jwt_required()]

    def get(self):
        return maquinas()


    def post(self):
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
