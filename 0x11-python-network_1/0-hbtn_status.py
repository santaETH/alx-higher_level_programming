#!/usr/bin/python30
"""A script that fetches 
- https://alx-intranet.hbtn.io/status
- using urllib package.
"""

if __name__ == "__main__":
    import urllib.request
    import sys

with  url.request..urlopen('https://alx-intranet.hbtn.io/status') as res:
            content = res.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
