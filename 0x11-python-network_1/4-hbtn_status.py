#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
- You must use the package requests
- You are not allow to import packages other than requests
- The body of the response must be display like the following example
"""
import request


if __name__ == "__main__":
    response = request.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
