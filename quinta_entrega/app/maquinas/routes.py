from flask import Blueprint
from app.maquinas.controllers import MaquinasGeral, MaquinasParticular

# MaquinasGeral: 
# - ver lista de maquinas 
# - adicionar maquina
# MaquinasParticular: 
# - ver detalhes de uma maquina 
# - editar maquina 
# - detelar maquina

maquinas_api = Blueprint('maquinas_api', __name__)

maquinas_api.add_url_rule('/maquinas', 
        view_func=MaquinasGeral.as_view('maquinas_geral'), 
        methods=['GET', 'POST'])

maquinas_api.add_url_rule('/maquina/<int:id_escolhido>', 
        view_func=MaquinasParticular.as_view('maquinas_particular'), 
        methods=['GET', 'PATCH', 'DELETE'])