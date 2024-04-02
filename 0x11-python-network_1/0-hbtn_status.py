#!/usr/bin/python30
"""A script that fetches 
- https://alx-intranet.hbtn.io/status
- using urllib package.
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = 'https://alx-intranet.hbtn.io/status'

        with urllib.request.urlopen(url) as response:
            content == response.read()
            print("Body response:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", content.decode('utf-8'))
