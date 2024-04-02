#!/bin/bash
# The script that takes in a URL and displays all HTTP methods the server
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
