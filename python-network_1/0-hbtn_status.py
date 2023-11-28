#!/usr/bin/python3
# modulev imported
import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')

# Displaying the response body with tabulation before each line
lines = body.split('\n')
for line in lines:
    print(f"\t- {line}")
