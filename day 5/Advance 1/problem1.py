'''
1. Write a program to open three files 1.txt, 2.txt and 3.txt 
if any these files are not present, a message without 
exiting the program must be printed prompting the same. 
'''

files = ['1.txt', '2.txt', '3.txt']

for file_name in files:
    try:
        with open(file_name, 'r') as f:
            print(f"Successfully opened {file_name}")
    except FileNotFoundError:
        # We print a message but the loop continues to the next file
        print(f"Message: The file '{file_name}' was not found.")