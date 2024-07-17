from accessor import github_accessor
import base64


def get_commit_sha(git_installation_token: str, owner: str, repo: str, ref: str) -> str:
    commit = github_accessor.get_latest_commit(
        git_installation_token=git_installation_token,
        owner=owner,
        repo=repo,
        ref="heads/main",
    )
    return commit["sha"]


def get_file_paths(
    git_installation_token: str, owner: str, repo: str, sha: str
) -> list[str]:
    tree = github_accessor.get_tree(
        git_installation_token=git_installation_token,
        owner=owner,
        repo=repo,
        sha=sha,
    )
    tree_paths = tree["tree"]
    return [
        tree_path["path"]
        for tree_path in tree_paths
        if tree_path["path"].startswith("src")
        and tree_path["path"] != "src"
        and tree_path["path"].endswith(".md")
    ]


def get_repo_content(
    git_installation_token: str, owner: str, repo: str, path: str
) -> str:
    repo_content = github_accessor.get_repo_content(
        git_installation_token=git_installation_token, owner=owner, repo=repo
    )
    encoded_content = repo_content["content"]
    decoded_content_bytes = base64.b64decode(encoded_content)
    return decoded_content_bytes.decode("utf-8")
