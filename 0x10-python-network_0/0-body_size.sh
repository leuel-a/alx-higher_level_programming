#!/usr/bin/env bash
# Takes a URL, sends a request to that URL, and displays the size of the body of the response

if [ $# -ne 1 ]
then
    echo "Usage: 0-body_size.sh [URL]"
else
    curl -w '%{size_download}' -o /dev/null -s "$1" ; echo ""
fi