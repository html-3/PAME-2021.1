from flask import request, jsonify
from flask.views import MethodView
from app.maquinas.utils import maquinas, maquina_utilidades
from sqlalchemy import exc
from app.extensions import db
from app.maquinas.model import Maquina
from app.funcionarios.model import Funcionario
from datetime import date, datetime

class MaquinasGeral(MethodView): # /maquinas

    def get(self):
        return maquinas()


    def post(self):
        dados = request.json
        return maquina_utilidades(dados, 0, "POST")

class MaquinasParticular(MethodView): # /maquina/<int:id_escolhido>
    
    def get(self, id_escolhido):
        return maquina_utilidades(0, id_escolhido, "GET")

    def patch(self, id_escolhido):
        dados = request.json
        return maquina_utilidades(dados, id_escolhido, "PATCH")
    
    def delete(self, id_escolhido):
        return maquina_utilidades(0, id_escolhido, "DELETE")
