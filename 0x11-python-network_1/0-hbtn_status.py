#!/usr/bin/python3
"""A script that fetches 
- https://alx-intranet.hbtn.io/status
- uing urllib package.
"""


import urllib.request
import sys

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content == response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode(''utf-8))
except urllib.error.URLError as e:
    print("Error:", e.reason)
    sys.exit(1)
