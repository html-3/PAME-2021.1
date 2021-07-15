from flask import request
from flask.views import MethodView
from app.funcionarios.utils import funcionarios, funcionario_utilidades

class FuncionariosGeral(MethodView): # /funcionarios

    def get(self):
        return funcionarios()


    def post(self):
        dados = request.json
        return funcionario_utilidades(dados, 0, "POST")

class FuncionariosParcicular(MethodView): # /funcionario/<int:id_escolhido>
    
    def get(self, id_escolhido):
        return funcionario_utilidades(0, id_escolhido, "GET")

    def patch(self, id_escolhido):
        dados = request.json
        return funcionario_utilidades(dados, id_escolhido, "PATCH")
    

    def delete(self, id_escolhido):
        return funcionario_utilidades(0, id_escolhido, "DELETE")
