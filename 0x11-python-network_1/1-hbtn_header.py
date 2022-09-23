#!/usr/bin/python3
"""
Contains a script that sends a request to a url
and displays the value of 'X-Request-Id' variable
in the header response.
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
