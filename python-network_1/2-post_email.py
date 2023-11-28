#!/usr/bin/python3
""" A script that sends POST request
"""


if __name__ == '__main__':
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys
    data = urlencode({"email": sys.argv[2]
                      }).encode("ascii")

    request = Request(sys.argv[1], data)
    with urlopen(request) as response:
        print(response.read().decode('utf-8'))
