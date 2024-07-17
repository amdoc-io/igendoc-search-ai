from flask import Blueprint
from .hello_api import hello_api_blueprint
from .train_doc_api import train_doc_api_blueprint
from .generate_ai_response_api import generate_ai_response_api_blueprint


def register_all_apis(app):
    app.register_blueprint(hello_api_blueprint, url_prefix="/v1")
    app.register_blueprint(train_doc_api_blueprint, url_prefix="/v1")
    app.register_blueprint(generate_ai_response_api_blueprint, url_prefix="/v1")
