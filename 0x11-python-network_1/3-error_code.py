#!/usr/bin/python3
"""
A python script that takes in a URL, sends a req to
URL and displays the body of the resp (decoded in utf-8).
"""


from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code": {e.code}")
