from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import exc
from app.extensions import db
from app.registros.model import Registro
from app.maquinas.model import Maquina
from app.registros.utils import temperaturas, temperatura_utilidades, pesos, peso_utilidades

class TemperaturaGeral(MethodView): # /temperaturas

    def get(self):
        temperaturas()

    def post(self):
        dados = request.json
        temperatura_utilidades(dados, None, "POST")

class TemperaturaParticular(MethodView): # /temperatura/<int:id_escolhido>

    def get(self, id_escolhido):
        temperatura_utilidades(None, id_escolhido, "GET")

    def patch(self, id_escolhido):
        dados = request.json
        temperatura_utilidades(dados, id_escolhido, "PATCH")

    def delete(self, id_escolhido):
        temperatura_utilidades(None, id_escolhido, "DELETE")


class PesoGeral(MethodView): # /pesos

    def get(self):
        pesos()

    def post(self):
        dados = request.json
        peso_utilidades(dados, None, "POST")

class PesoParticular(MethodView): # /peso/<int:id_escolhido>

    def get(self, id_escolhido):
        peso_utilidades(None, id_escolhido, "GET")

    def patch(self, id_escolhido):
        dados = request.json
        peso_utilidades(dados, id_escolhido, "PATCH")

    def delete(self, id_escolhido):
        peso_utilidades(None, id_escolhido, "DELETE")
