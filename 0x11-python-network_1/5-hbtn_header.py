#!/usr/bin/python3
""""The script that takes in a URL, sends a req to the URL
and disp the value of the variable X-Request-Id in the resp header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
