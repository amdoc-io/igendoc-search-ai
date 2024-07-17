from flask import Blueprint
from .hello_api import hello_api_blueprint


def register_all_apis(app):
    app.register_blueprint(hello_api_blueprint, url_prefix="/v1")
