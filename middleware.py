from flask import request, jsonify


def middleware():
    if request.endpoint == "train_doc_api_blueprint.train_doc":
        git_installation_token = request.headers.get("X-Git-Installation-Token")
        if not git_installation_token:
            return (
                jsonify(
                    {"error": "Authorized: Missing X-Git-Installation-Token header"}
                ),
                401,
            )
