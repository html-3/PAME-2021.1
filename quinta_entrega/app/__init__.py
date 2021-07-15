from flask import Flask
from .extensions import db, migrate, mail, jwt
from .config import Config
from .funcionarios.routes import funcionarios_api
from .maquinas.routes import maquinas_api
from .registros.routes import registros_api
from dummy_data import create_dd

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    
    jwt.init_app(app)

    create_dd(app)

    app.register_blueprint(funcionarios_api)
    app.register_blueprint(maquinas_api)
    app.register_blueprint(registros_api)

    return app
