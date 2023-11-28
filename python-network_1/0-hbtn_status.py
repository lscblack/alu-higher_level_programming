#!/usr/bin/python3
"""
This script demonstrates fetching content from a URL using urllib.

It fetches content from 'https://intranet.hbtn.io/status' using urllib and displays information about the response body.
"""

import urllib.request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
