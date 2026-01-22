import os
import sys

file_path = "/home/phonemyattayzarkyaw/py-linux-auto/backup_log.txt"

try:
    with open(file_path, "r") as f:
        content = f.read()
    print(f"File content:")
    print(content)
except FileNotFoundError:
    print(f"ERROR: File not found: {file_path}")
except Exception as e:
    print(f"Error: {e}")