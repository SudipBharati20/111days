'''
2. Write a program to print third, fifth and seventh element 
from a list using enumerate function. 
'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index, value in enumerate(my_list):
    # index 2 = 3rd element, index 4 = 5th element, index 6 = 7th element
    if index in [2, 4, 6]:
        print(f"Element {index + 1}: {value}")