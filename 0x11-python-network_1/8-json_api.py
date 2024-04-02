#!/usr/bin/python3
"""
Python script that takes in a URL, sends a 
request to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check the status code
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Print the body of the response
        print(response.text)
