from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    #migrate.init_app(app, db)

    app.config.from_object(Config)

    return app
