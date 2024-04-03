#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a req to the URL
and displays the value of the X-Request-Id.
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
