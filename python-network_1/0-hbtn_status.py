#!/usr/bin/python3
"""
documented by no
"""

import urllib.request

if __name__ == '__main__':
    # First request without headers
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("First Request - Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))

    # Second request with headers
    url = 'https://alu-intranet.hbtn.io/status'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("\nSecond Request - Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
