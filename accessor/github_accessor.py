import requests

BASE_URL = "https://api.github.com"


def get_latest_commit(git_installation_token: str, owner: str, repo: str, ref: str):
    url = "{}/repos/{}/{}/commits/{}".format(BASE_URL, owner, repo, ref)
    headers = {
        "Authorization": "Bearer {}".format(git_installation_token),
        "Content-Type": "application/json",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_tree(git_installation_token: str, owner: str, repo: str, sha: str):
    url = "{}/repos/{}/{}/git/trees/{}".format(BASE_URL, owner, repo, sha)
    params = {
        "recursive": "true",
    }
    headers = {
        "Authorization": "Bearer {}".format(git_installation_token),
        "Content-Type": "application/json",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
