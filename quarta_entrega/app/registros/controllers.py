from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import exc
from app.extensions import db
from app.registros.model import Registro
from app.maquinas.model import Maquina

class RegistrosGeral(MethodView): # /registro

    def get(self):
        registros = Registro.query.all()
        
        return jsonify([registro.json() for registro in registros]), 200


    def post(self):
        if True:
            dados = request.json

            try:
                horario = dados.get('horario')
                temperatura = float(dados.get('temperatura'))
                peso_medio = float(dados.get('peso_medio'))
                maquina_id = int(dados.get('cargo'))

                maquina = Maquina.query.get_or_404(maquina_id)

                registro = Registro(horario=horario,
                                    temperatura=temperatura,
                                    peso_medio=peso_medio,
                                    maquina=maquina)

                db.session.add(registro)
                db.session.commit()

            # com a funcao str(), obriga o input ser uma string, ou convertivel para uma string
            except ValueError:
                return {'error': 'tipo invalido'}, 400

            # erro de integridade
            except exc.IntegrityError:
                db.session.rollback()
                return {'error': 'erro de integridade'}, 400

            # pegar oustros erros quaisquer (nunca disparou mas nunca se sabe)
            except:
                return {'error': 'ocorreu um erro'}, 400
            
        return registro.json(), 200


    def delete(self):
        dados = request.json

        id_registro = dados.get('id_registro')

        if not id_registro or not isinstance(id_registro, int):
            return {'error': 'id_registro nao foi declarado ou invalido'}, 400

        registro = Registro.query.get_or_404(id_registro)
        try:
            db.session.delete(registro)

            db.session.commit()

        except:
            return {'error': 'registro nao existe'}, 400

        return registro.json(), 200
