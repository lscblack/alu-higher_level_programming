#!/usr/bin/python3
"""
This script demonstrates fetching content from a URL using urllib.

It fetches content from 'https://intranet.hbtn.io/status' using urllib and displays information about the response body.
"""

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content.decode("utf-8")))