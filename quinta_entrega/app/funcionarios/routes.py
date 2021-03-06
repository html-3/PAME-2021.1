from flask import Blueprint
from app.funcionarios.controllers import FuncionariosGeral, FuncionariosParcicular, FuncionariosLogin

# FuncionariosLogin:
# - enviar dados de login
# FuncionariosGeral: 
# - ver lista de funcionarios 
# - adicionar funcionario
# FuncionariosParcicular: 
# - ver detalhes de um funcionario 
# - reescrever detalhes de um funcionario
# - editar funcionario 
# - detelar funcionario

funcionarios_api = Blueprint('funcionarios_api', __name__)

funcionarios_api.add_url_rule('/login', 
        view_func=FuncionariosLogin.as_view('funcionarios_login'), 
        methods=['POST'])

funcionarios_api.add_url_rule('/funcionarios', 
        view_func=FuncionariosGeral.as_view('funcionarios_geral'), 
        methods=['GET', 'POST'])

funcionarios_api.add_url_rule('/funcionario/<int:id_escolhido>', 
        view_func=FuncionariosParcicular.as_view('funcionarios_particular'), 
        methods=['GET', 'PATCH', 'DELETE'])