#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)

"""
import sys
import urllib.request
import urllib.parse


def main():
    """Entry point of program"""
    url = sys.argv[1]
    values = {
        'email': sys.argv[2]
        }

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        response_data = response.read()

    print(response_data.decode('utf-8'))


if __name__ == '__main__':
    main()
