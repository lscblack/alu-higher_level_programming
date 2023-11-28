 #!/usr/bin/python3
import urllib.request
""" docuemhjf """
if __name__ == '__main__':
    url1 = 'https://alu-intranet.hbtn.io/status'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    req = urllib.request.Request(url1, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("First Request - Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))

    url2 = 'http://0.0.0.0:5050/status'
    with urllib.request.urlopen(url2) as response:
        content = response.read()
        print("\nSecond Request - Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
