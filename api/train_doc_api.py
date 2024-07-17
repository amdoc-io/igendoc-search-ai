from flask import jsonify, Blueprint, request
from builder import github_builder

train_doc_api_blueprint = Blueprint("train_doc_api_blueprint", __name__)


@train_doc_api_blueprint.route("/train-doc", methods=["POST"])
def train_doc():
    git_installation_token = request.headers.get("X-Git-Installation-Token")
    body = request.get_json()
    owner = body["owner"]
    repo = body["repo"]

    sha = github_builder.get_commit_sha(
        git_installation_token=git_installation_token,
        owner=owner,
        repo=repo,
        ref="heads/main",
    )
    file_paths = github_builder.get_file_paths(
        git_installation_token=git_installation_token,
        owner=owner,
        repo=repo,
        sha=sha,
    )
    contents = github_builder.get_repo_contents(
        git_installation_token=git_installation_token,
        owner=owner,
        repo=repo,
        paths=file_paths,
    )

    data = {
        "body": body,
        "git_installation_token": git_installation_token,
        "sha": sha,
        "file_paths": file_paths,
        "contents": contents,
    }
    return jsonify(data), 200
