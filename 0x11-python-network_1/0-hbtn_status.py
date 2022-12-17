#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


def main() -> None:
    """Entry point to my program"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        response_data = response.read()

    utf_c = response_data.decode("utf-8")
    print("Body response: \n" \
        f"    - type: {type(response_data)}\n"\
        f"    - content: {response_data}\n"\
        f"    - utf-8 content: {utf_c}")

if __name__ == '__main__':
    main()
