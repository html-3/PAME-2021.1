from app import create_app
from dummy_data import criar_db

# condicao permite que o app apenas seja inicializado dentro de este documento
if __name__ == "__main__":
    # instanciacao do app neste local
    app = create_app()

    # cria uma database
    # gera dados ficticios para preencher este banco de dados
    criar_db(app) 

    # metodo do flask que efetivamente inicia o aplicativo
    app.run()