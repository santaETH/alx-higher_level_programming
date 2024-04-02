#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.
- The first argument will be the repository name
- The second argument will be the owner name
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    r =requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".frmat(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
