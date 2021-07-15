from flask import Blueprint
from app.registros.controllers import RegistrosGeral

# RegistrosGeral: 
# - lista de registros
# - adicionar registro
# - deleter registro

registros_api = Blueprint('registros_api', __name__)

registros_api.add_url_rule('/registros', 
        view_func=RegistrosGeral.as_view('registros_geral'), 
        methods=['GET', 'POST', 'DELETE'])