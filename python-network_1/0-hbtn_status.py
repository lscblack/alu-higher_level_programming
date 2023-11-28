#!/usr/bin/python3
"""
This script demonstrates fetching content from a URL using urllib.

It fetches content from 'https://intranet.hbtn.io/status' using urllib and displays information about the response body.
"""

import urllib.request

if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))