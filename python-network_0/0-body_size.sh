#!/bin/bash
# takes URL and displays the size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
