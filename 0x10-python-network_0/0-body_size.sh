#!/bin/bash
# Takes a URL, sends a request to that URL, and displays the size of the body of the response
curl -w '%{size_download}' -o /dev/null -s "$1" ; echo ""
