#!/usr/bin/python3
"""Documented"""


import urllib.request

def fetch_and_display(url, expected_output):
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
        if content.decode("utf-8") == expected_output:
            print("(Expected output matched)")
        else:
            print("(Expected output NOT matched)")

if __name__ == '__main__':
    # Fetching 'https://intranet.hbtn.io/status'
    url_1 = 'https://intranet.hbtn.io/status'
    expected_output_1 = 'OK'
    fetch_and_display(url_1, expected_output_1)

    # Fetching 'http://0.0.0.0:5050/status'
    url_2 = 'http://0.0.0.0:5050/status'
    expected_output_2 = 'Custom status'
    fetch_and_display(url_2, expected_output_2)
