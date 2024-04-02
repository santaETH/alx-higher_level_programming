#!/usr/bin/python3
"""
A ython script that takes in a URL, sends a request to the 
URL and displays the body of the response (decoded in utf-8).
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
