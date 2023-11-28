#!/usr/bin/python3
"""send request."""
import urllib.request
import urllib.error
import sys


def send_request():
    """Send request."""
    try:
        with urllib.request.urlopen(sys.argv[1]) as re:
            xyz = re.read()
            print(xyz.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))

if __name__ == "__main__":
    send_request()
