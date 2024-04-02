#!/bin/bash
# The secript that sends a request to a url passed as an argument and displays onluy status of response
curl -so /dev/null -w "%{http_code}" "$1"
