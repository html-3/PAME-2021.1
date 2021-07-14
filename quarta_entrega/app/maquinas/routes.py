from app.maquinas.controllers import MaquinasGeral
from flask import Blueprint
from app.maquinas.controllers import MaquinasGeral, MaquinasParticular, MaquinasOperadores

# MaquinasGeral: 
# - lista de maquinas 
# - adicionar maquina
# MaquinasParticular: 
# - ver detalhes de uma maquina 
# - reescrever detalhes de uma maquina 
# - editar maquina 
# - detelar maquina
# MaquinasOperadores: 
# - ver operadores de uma maquina 
# - adicionar operador de uma maquina 
# - remover operador

maquinas_api = Blueprint('maquinas_api', __name__)

maquinas_api.add_url_rule('/maquinas', 
        view_func=MaquinasGeral.as_view('maquinas_geral'), 
        methods=['GET', 'POST'])

maquinas_api.add_url_rule('/maquina/<int:id_escolhido>', 
        view_func=MaquinasParticular.as_view('maquinas_particular'), 
        methods=['GET', 'PUT', 'PATCH', 'DELETE'])

maquinas_api.add_url_rule('/maquina/<int:id_maquina>/operadores', 
        view_func=MaquinasOperadores.as_view('maquinas_operadores'), 
        methods=['GET', 'POST', 'DELETE'])