from flask import Flask
import os
import dotenv
import click
from data.seeding import seed_database
from main.routes import main
from apis.routes import api_bp
from api.routes import api
from extensions import db, migrate


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Load environmental variables:
    DOTENV_BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                  os.pardir, "instance"))
    dotenv.load_dotenv(os.path.join(DOTENV_BASEDIR, "database.env"))

    # Set up Keys:
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY") or 'dev',
        SQLALCHEMY_DATABASE_URI=os.getenv("DEPLOYMENT_DATABASE") or
        os.getenv("PRODUCTION_DATABASE") or
        "sqlite:///app.db"
    )

    # Configure custom command "flask seeding"
    @app.cli.command("seeding")
    @click.argument("number_of_arguments")
    def seeding(number_of_arguments):
        seed_database(number_of_arguments)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(api_bp)
    app.register_blueprint(api)

    # Database
    db.init_app(app)
    migrate.init_app(app, db)

    return app
