#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"

if (os.path.isfile(file)):
    data = load_from_json_file(file)
    data.extend(sys.argv[1:])
else:
    data = []
    data.extend(sys.argv[1:])
save_to_json_file(data, file)
