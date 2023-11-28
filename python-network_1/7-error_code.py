#!/usr/bin/python3
"""A script that sends a requests and displays the body of response."""


if __name__ == '__main__':
    import requests
    import sys
    request = requests.get(sys.argv[1])
    if request.status_code < 400:
        print(request.text)
    elif request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
