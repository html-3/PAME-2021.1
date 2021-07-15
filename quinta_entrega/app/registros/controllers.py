from flask import request
from flask.views import MethodView
from app.registros.utils import temperaturas, temperatura_utilidades, pesos, peso_utilidades
from flask_jwt_extended import jwt_required

class TemperaturaGeral(MethodView): # /temperaturas
    decorators = [jwt_required()]

    def get(self):
        return temperaturas()

    def post(self):
        dados = request.json
        return temperatura_utilidades(dados, 0, "POST")

class TemperaturaParticular(MethodView): # /temperatura/<int:id_escolhido>
    decorators = [jwt_required()]

    def get(self, id_escolhido):
        return temperatura_utilidades(0, id_escolhido, "GET")

    def patch(self, id_escolhido):
        dados = request.json
        return temperatura_utilidades(dados, id_escolhido, "PATCH")

    def delete(self, id_escolhido):
        return temperatura_utilidades(0, id_escolhido, "DELETE")


class PesoGeral(MethodView): # /pesos
    decorators = [jwt_required()]

    def get(self):
        return pesos()

    def post(self):
        dados = request.json
        return peso_utilidades(dados, 0, "POST")

class PesoParticular(MethodView): # /peso/<int:id_escolhido>
    decorators = [jwt_required()]

    def get(self, id_escolhido):
        return peso_utilidades(0, id_escolhido, "GET")

    def patch(self, id_escolhido):
        dados = request.json
        return peso_utilidades(dados, id_escolhido, "PATCH")

    def delete(self, id_escolhido):
        return peso_utilidades(0, id_escolhido, "DELETE")
