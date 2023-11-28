#!/usr/bin/python3
"""Request to the URL and displays the value of the variable."""


if __name__ == "__main__":
    import requests
    import sys

    respo = requests.get(sys.argv[1])
    header_var = respo.headers.get('X-Request-Id')
    print(header_var)
