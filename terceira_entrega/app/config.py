import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    # permite melhor testagem do app
    # retornar False depois do desenvolvimento
    DEBUG = True

    # configuracao da database (modo web-dev)
    SQLALCHEMY_DATABASE_URI = "sqlite:///data-dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # configuracao da comunicacao com o front-end
    JSON_SORT_KEYS = False