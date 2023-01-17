#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.

"""
import sys
import urllib.request


def main():
    """Entry point of program"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        response_header = response.headers

    print(dict(response_header).get('X-Request-Id'))


if __name__ == '__main__':
    main()
