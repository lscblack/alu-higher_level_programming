#!/usr/bin/python3
"""A script that displays the value of the x-request ID."""


if __name__ == '__main__':
    from urllib.request import urlopen
    import sys

    with urlopen(sys.argv[1]) as re:
        header_var = re.headers.get('X-Request-Id')
        print(header_var)
