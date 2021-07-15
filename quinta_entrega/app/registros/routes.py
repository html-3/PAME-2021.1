from flask import Blueprint
from app.registros.controllers import TemperaturaGeral, TemperaturaParticular, PesoGeral, PesoParticular

registros_api = Blueprint('registros_api', __name__)

registros_api.add_url_rule('/temperaturas', 
        view_func=TemperaturaGeral.as_view('temperatura_geral'), 
        methods=['GET', 'POST'])

registros_api.add_url_rule('/temperatura/<int:id_escolhido>', 
        view_func=TemperaturaParticular.as_view('temperatura_particular'), 
        methods=['GET', 'PATCH', 'DELETE'])

registros_api.add_url_rule('/pesos', 
        view_func=PesoGeral.as_view('peso_geral'), 
        methods=['GET', 'POST'])

registros_api.add_url_rule('/peso/<int:id_escolhido>', 
        view_func=PesoParticular.as_view('peso_particular'), 
        methods=['GET', 'PATCH', 'DELETE'])