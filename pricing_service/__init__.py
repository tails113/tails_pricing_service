from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config


db = SQLAlchemy()


def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    with app.app_context():
        import pricing_service.api.models
        db.create_all()


def register_blueprints(app):
    from pricing_service.api.views import api
    app.register_blueprint(api, url_prefix='/api')
