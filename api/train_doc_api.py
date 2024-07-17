from flask import jsonify, Blueprint, request
from accessor import github_accessor

train_doc_api_blueprint = Blueprint("train_doc_api_blueprint", __name__)


@train_doc_api_blueprint.route("/train-doc", methods=["POST"])
def train_doc():
    git_installation_token = request.headers.get("X-Git-Installation-Token")
    body = request.get_json()
    owner = body["owner"]
    repo = body["repo"]

    commit = github_accessor.getCommit(
        git_installation_token=git_installation_token,
        owner=owner,
        repo=repo,
        ref="heads/main",
    )
    tree = github_accessor.get_tree(
        git_installation_token=git_installation_token,
        owner=owner,
        repo=repo,
        sha=commit["sha"],
    )

    data = {
        "message": {
            "body": body,
            "git_installation_token": git_installation_token,
            "commit": commit,
            "tree": tree,
        }
    }
    return jsonify(data), 200
