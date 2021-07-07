from flask import request, Blueprint
from model import Medico
from app.extensions import db

# sufixo -I significa instanciacao

medico_api = Blueprint('medico_api', __name__)

@medico_api.route('/medicos', methods=['POST'])
def criar_medico():
    
    if request.method == "POST":
        dados = request.json
        nomeI = dados.get("nome")
        espI = dados.get("esp")

        # no caso que nao seja submetido nenhum, celular ou email
        try:
            celI = dados.get("cel")
            emailI = dados.get("email")

            if not isinstance(nomeI, str) or \
               not isinstance(espI, str) or \
               not isinstance(celI, str) or \
               not isinstance(emailI, str):
               return {'error': 'tipo invalido'}, 400

            medicoI = Medico(nome=nomeI,
                             esp=espI,
                             cel=celI,
                             email=emailI
                            )
        except:
            if not isinstance(nomeI, str) or \
               not isinstance(espI, str):
               return {'error': 'tipo invalido'}, 400

            medicoI = Medico(nome=nomeI,
                             esp=espI
                            )


        db.session.add(medicoI)
        db.session.commit()

        return medicoI.json(), 200

    else:
        return {'error': 'metodo invalido'}, 405


        