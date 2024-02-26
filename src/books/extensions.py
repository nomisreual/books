from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
api = Api()


def login_manager():
    login = LoginManager()
    login.login_view = "auth.login"

    return login


login = login_manager()
