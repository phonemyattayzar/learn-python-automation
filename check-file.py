import os
import sys

file_path = "config.json"

if os.path.isfile(file_path):
    print(f"{file_path} exists")
else:
    print(f"{file_path} not exists")
    sys.exit(1)