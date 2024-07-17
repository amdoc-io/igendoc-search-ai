from flask import jsonify, Blueprint

hello_api_blueprint = Blueprint("hello_api_blueprint", __name__)


@hello_api_blueprint.route("/hello")
def hello():
    data = {"message": "Hello, world!"}
    return jsonify(data)
