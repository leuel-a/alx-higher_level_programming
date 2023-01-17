#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


def main() -> None:
    """Entry point to my program"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        response_data = response.read()

    utf_content = response_data.decode("utf-8")
    print("Body response:")
    print(f"\t- type: {type(response_data)}")
    print(f"\t- content: {response_data}")
    print(f"\t- utf8 content: {utf_content}")


if __name__ == '__main__':
    main()
