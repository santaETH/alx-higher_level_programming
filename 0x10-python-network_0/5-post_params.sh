#!/bin/bash
# The script that takes the url and sends a post request
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
