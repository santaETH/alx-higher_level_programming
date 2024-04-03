#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to disp your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)

    response = requests.get('https://api.github.com/user', auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)
