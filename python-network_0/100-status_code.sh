#!/bin/bash
# A Bash script that sends a request to a url passed as an argument,and displays only the status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
