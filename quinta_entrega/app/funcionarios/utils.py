from flask import jsonify, render_template
from app.extensions import db
from app.funcionarios.model import Funcionario
from sqlalchemy import exc
from flask_jwt_extended import create_access_token
import bcrypt
from flask_mail import Message

# aqui as funcionalidades dos metodos e outras funcoes sao definidas
# tambem sao feitos os testes de validacao dos dados, para enviar os erros ao front

# funcao para enviar email
def email_login(nome, email, cargo):
    msg = Message(sender='email@email.com',
                  recipients=[email],
                  subject='Login efetuado!',
                  html=render_template('email.html', nome=nome, email=email, cargo=cargo))

# funcao para efetuar login
def login(dados):
    try:
        email = dados.get('email')
        senha = dados.get('senha')
        
        if email == None or senha == None:
            return {'error': 'faltou algum dado'}, 400

        email = str(email)[0:30]
        senha = str(senha)[0:50]

        usuario = Funcionario.query.filter_by(email=email).first()

        if not usuario or not bcrypt.checkpw(senha.encode(), usuario.senha_hash):
            return {'error': 'email ou senha inválido'}, 400

        else:
            token_acesso = create_access_token(identity=usuario.id)
            return {'token': token_acesso}, 200

    except TypeError:
        return {'error': 'tipo inválido de nome, email, senha ou cargo'}, 400

    except ValueError:
        return {'error': 'tipo inválido de nome, email, senha ou cargo'}, 400
        
    except exc.IntegrityError:
        db.session.rollback()
        return {'error': 'banco de dados comprometido'}, 400

    except:
        return {'error': 'ocorreu um erro'}, 400

# funcao para listar todos os funcionarios
def funcionarios():
    funcionarios = Funcionario.query.all()

    return jsonify([funcionario.json() for funcionario in funcionarios]), 200

# funcao composta para ver, adicionar, editar e deletar funcionarios
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
            adm = dados.get('adm', funcionario.adm)

        elif metodo == "POST":
            nome = dados.get('nome')
            email = dados.get('email')
            senha = dados.get('senha', Funcionario.senha_base)
            cargo = dados.get('cargo', Funcionario.cargo_base)
            adm = dados.get('adm', Funcionario.adm_base)

        if nome == None or\
           email == None or\
           senha == None or\
           cargo == None or\
           adm == None:
            return {'error': 'faltou algum dado'}, 400

        if not isinstance(nome , str) or\
           not isinstance(email , str) or\
           not isinstance(senha , str) or\
           not isinstance(cargo , str):
           return {'error': 'dados devem ser string'}, 400

        if not isinstance(adm, bool):
            return {'error': 'cargo adm inválido'}, 400

        if senha == Funcionario.senha_base and metodo == "PATCH":
            senha_hash = funcionario.senha_hash
        
        else:
            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

        nome = str(nome)[0:30]
        email = str(email)[0:30]
        senha_hash = str(senha_hash)[0:100]
        cargo = str(cargo)[0:30]

        if metodo == "POST":

            if Funcionario.query.filter_by(email=email).first():
                return {'error': 'email deve ser unico'}, 400

            funcionario = Funcionario(nome=nome,
                                      email=email,
                                      senha_hash=senha_hash,
                                      cargo=cargo,
                                      adm=adm)
            db.session.add(funcionario)

            email_login(nome, email, cargo)

        if metodo == "PATCH":
            funcionario.nome = nome
            funcionario.email = email
            funcionario.senha_hash = senha_hash
            funcionario.cargo = cargo
            funcionario.adm = adm

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