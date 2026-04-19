"""
FILE HANDLING PROBLEM
"""

files = ["1.txt", "2.txt", "3.txt"]

for f in files:
    try:
        with open(f, "r") as file:
            print(f"{f} opened")
    except FileNotFoundError:
        print(f"{f} not found")