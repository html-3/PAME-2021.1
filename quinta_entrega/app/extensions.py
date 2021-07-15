from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_jwt_extended import JWTManager

# bcrypt foi pego da versao normal do python, nao da versao flask

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
jwt = JWTManager()