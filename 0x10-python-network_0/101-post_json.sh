#!/bin/bash
# The script that sends a JSON request to a url passed as the first argument and display body of response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
