from flask import jsonify, Blueprint, request

train_doc_api_blueprint = Blueprint("train_doc_api_blueprint", __name__)


@train_doc_api_blueprint.route("/train-doc", methods=["POST"])
def train_doc():
    git_installation_token = request.headers.get("X-Git-Installation-Token")

    body = request.get_json()
    data = {"message": {"body": body, "git_installation_token": git_installation_token}}
    return jsonify(data), 200
