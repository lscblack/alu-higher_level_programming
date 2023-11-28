#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status

- You must use the package urllib
- You are not allowed to import any packages other than urllib
- The body of the response must be displayed like the following example
(tabulation before -)
- You must use a with statement
urllib info --> https://docs.python.org/3/howto/urllib2.html
Info abour decode --> https://stackoverflow.com/questions/38807809/fetching-url
-and-converting-to-utf-8-python
"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))
