#!/usr/bin/python3
"""
Python script that takes in a URL, sends a
req to the URL and disp the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    try:
        response = requests.post(
                'http://0.0.0.0:5000/search_user', 
                data={'q': q}
        )
        data = response.json()

        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
