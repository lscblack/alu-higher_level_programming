#!/usr/bin/python3
"""Documented"""

import urllib.request

# URL to fetch
url = 'https://alu-intranet.hbtn.io/status'

# Creating a request object with the URL
req = urllib.request.Request(url)

# Making the request and reading the response body
with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')

# Displaying the response body with tabulation before each line
lines = body.split('\n')
for line in lines:
    print(f"\t- {line}")

