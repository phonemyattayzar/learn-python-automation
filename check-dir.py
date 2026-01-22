import os
import sys

dir_path = "/home/phonemyattayzarkyaw/check-dir"

if not os.path.isdir(dir_path):
    print(f"Directory Not Found: {dir_path}")
    user_input = input(f"I will create {dir_path} for you: y/n: ").strip().lower()
    if user_input == "y":
        os.makedirs(dir_path)
        print(f"Directory {dir_path} is successfully created")
    elif user_input == "n":
        print(f"Ok I will not create the directory {dir_path} for you")
        sys.exit(0)
    else:
        print(f"Invalid input. Please enter y or n.")
        sys.exit(1)
        
        

print(f"Directory Found, continue...")