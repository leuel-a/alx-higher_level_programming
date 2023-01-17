#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.error


def main():
    """Entry point of program"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            response_data = response.read()

        print(response_data.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")


if __name__ == '__main__':
    main()
