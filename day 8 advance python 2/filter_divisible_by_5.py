# File: filter_divisible_by_5.py

# Q4: Write a program to filter a list of numbers divisible by 5.

numbers = [10, 23, 45, 67, 50, 88, 55, 90]

# filter function
result = list(filter(lambda x: x % 5 == 0, numbers))

print("Numbers divisible by 5:", result)
