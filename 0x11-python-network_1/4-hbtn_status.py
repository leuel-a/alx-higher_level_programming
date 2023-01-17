#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def main():
    """Entry point of my program"""
    response = requests.get('https://alx-intranet.hbtn.io/status', timeout=1)
    print('Body response:')
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')


if __name__ == '__main__':
    main()
