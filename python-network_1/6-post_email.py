#!/usr/bin/python3
"""A script that sends POST requests and displays the response"""


if __name__ == '__main__':
    import requests
    import sys

    xyz = {'email': sys.argv[2]}
    request = requests.post(sys.argv[1], data=xyz)
    print("{}".format(request.text))
