#!/usr/bin/env python3

import os
from github import Github


def main():
    _github_token = os.getenv("GITHUB_TOKEN")
    _github_repo = os.getenv("GITHUB_REPOSITORY")
    _github_pr = int(os.getenv("PR_NUMBER"))
    _authorized = os.getenv("AUTHORIZED")
    repo = Github(_github_token).get_repo(_github_repo)
    pr = repo.get_pull(_github_pr)

    _username = pr.user.login

    if _username in _authorized:
        exit(0)

    print(f"Unauhtorized user: {_username}")
    exit(1)


if __name__ == "__main__":
    main()
