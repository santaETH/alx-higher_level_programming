#!/usr/bin/python3
"""
A ython script that takes in a URL, sends a request to the 
URL and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
import sys
import urllib.request
import urllib.error

try:
    with urllib.request.urlopen(url) as response:
        print(res.read().decode('utf-8'))
    except error.HTTPError as error:
        print('Error code:', error.code)
