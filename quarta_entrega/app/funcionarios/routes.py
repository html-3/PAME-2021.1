from flask import Blueprint
from app.funcionarios.controllers import FuncionariosGeral, FuncionariosParcicular

funcionarios_api = Blueprint('funcionarios_api', __name__)

funcionarios_api.add_url_rule('/funcionarios', 
        view_func=FuncionariosGeral.as_view('funcionarios_geral'), 
        methods=['GET', 'POST'])

funcionarios_api.add_url_rule('/funcionario/<int:id_escolhido>', 
        view_func=FuncionariosParcicular.as_view('funcionarios_particular'), 
        methods=['GET', 'PUT', 'PATCH', 'DELETE'])