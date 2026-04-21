# File: max_using_reduce.py

# Q5: Write a program to find maximum number in a list using reduce()

from functools import reduce

numbers = [12, 45, 67, 89, 23, 10]

# reduce to find maximum
maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum number is:", maximum)