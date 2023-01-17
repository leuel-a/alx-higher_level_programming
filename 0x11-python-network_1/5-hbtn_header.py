#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id
in the response header

"""
import sys
import requests


def main():
    """Entry point if program"""
    response = requests.get(sys.argv[1])
    print(dict(response.headers).get('X-Request-Id'))


if __name__ == '__main__':
    main()
