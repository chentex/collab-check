#!/usr/bin/env python3

import os
from github import Github


def main(*args):
    if len(args) != 4:
        print("Wrong number of arguments")
        return 1
    _github_token = args[0]
    _github_repo = args[1]
    _github_pr = args[2]
    _authorized = args[2]
    repo = Github(_github_token).get_repo(_github_repo)
    pr = repo.get_pull(_github_pr)

    _username = pr.user.name

    if _username in _authorized:
        return 0

    print(f"Unauhtorized user: {_username}")
    return 1


if __name__ == "__main__":
    main()
