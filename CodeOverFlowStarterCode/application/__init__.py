import os

from flask import Flask

# TODO: import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# TODO: import flask_login
from flask_login import LoginManager

from flask_wtf.csrf import CSRFProtect

from os import path

# TODO: declare sqlalchemy db here
db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config_template.Config")

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import Users, Expenses

    # TODO: initialise sqlalchemy db here
    db.init_app(app)

    # TODO: create sqlalchemy db file
    if not path.exists(app.config["DATABASE_NAME"]):  # check if db file exists
        db.create_all(app=app)
        print("Created Database!")

    # TODO: initialise loginmanager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(id)

    csrf.init_app(app)
    return app
