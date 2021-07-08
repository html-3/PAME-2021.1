from flask import Flask
from .config import Config
from .extensions import db, migrate

# funcao que cria o app
def create_app():

    # instanciacao do aplicativo
    app = Flask(__name__)

    # configuracao do app
    app.config.from_object(Config)

    # inicializacao da database
    db.init_app(app)

    migrate.init_app(app, db)

    return app
