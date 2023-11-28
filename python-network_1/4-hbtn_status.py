#!/usr/bin/python3
"""Python script that fetchs."""


import requests
if __name__ == "__main__":
    requ = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(requ.text)))
    print("\t- content: {}".format(requ.text))
