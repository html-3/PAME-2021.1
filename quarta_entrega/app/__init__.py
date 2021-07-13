from flask import Flask
from .extensions import db, migrate
from .config import Config
from dummu_data import create_dd

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    create_dd(app)

    return app
