from flask import jsonify
from app.extensions import db
from app.funcionarios.model import Funcionario
from sqlalchemy import exc
import bcrypt

# utilidades peso
def funcionarios():
    funcionarios = Funcionario.query.all()

    return jsonify([funcionario.json() for funcionario in funcionarios]), 200

def funcionario_utilidades(dados, id_escolhido, metodo):
    if not isinstance(id_escolhido, int):
        return {'error': 'id_escolhido inválido'}, 400
        
    if metodo in ["GET", "PATCH", "DELETE"]:
        funcionario = Funcionario.query.get_or_404(id_escolhido)

    if metodo == "GET":
        return funcionario.json(), 200

    if metodo == "DELETE":
        db.session.delete(funcionario)
        db.session.commit()

        return funcionario.json(), 200

    try:
        if metodo == "PATCH":
            nome = dados.get('nome', funcionario.nome)
            email = dados.get('email', funcionario.email)
            senha = dados.get('senha', Funcionario.senha_base)
            cargo = dados.get('cargo', funcionario.cargo)

        elif metodo == "POST":
            nome = dados.get('nome')
            email = dados.get('email')
            senha = dados.get('senha', Funcionario.senha_base)
            cargo = dados.get('cargo', Funcionario.cargo_base)

        if nome == None or\
           email == None or\
           senha == None or\
           cargo == None:
            return {'error': 'faltou algum dado'}, 400

        if not isinstance(nome , str) or\
           not isinstance(email , str) or\
           not isinstance(senha , str) or\
           not isinstance(cargo , str):
           return {'error': 'dados devem ser string'}, 400

        if senha == Funcionario.senha_base and metodo == "PATCH":
            senha_hash = funcionario.senha_hash
        
        else:
            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

        nome = str(nome)[0:30]
        email = str(email)[0:30]
        senha = str(senha)[0:50]
        cargo = str(cargo)[0:30]

        if metodo == "POST":

            if Funcionario.query.filter_by(email=email).first():
                return {'error': 'email deve ser unico'}, 400

            funcionario = Funcionario(nome=nome,
                                      email=email,
                                      senha=senha,
                                      cargo=cargo)
            db.session.add(funcionario)

        if metodo == "PATCH":
            funcionario.nome = nome
            funcionario.email = email
            funcionario.senha = senha
            funcionario.cargo = cargo

        db.session.commit()

    except TypeError:
        return {'error': 'tipo inválido de nome, email, senha ou cargo'}, 400

    except ValueError:
        return {'error': 'tipo inválido de nome, email, senha ou cargo'}, 400
        
    except exc.IntegrityError:
        db.session.rollback()
        return {'error': 'banco de dados comprometido'}, 400

    except:
        return {'error': 'ocorreu um erro'}, 400

    return funcionario.json(), 200