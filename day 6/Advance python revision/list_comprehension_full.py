"""
LIST COMPREHENSION
"""

nums = [1,2,3,4]

squares = [x*x for x in nums]
print(squares)

# ------------------ PROBLEMS ------------------

# Problem 1: Even numbers
evens = [x for x in nums if x % 2 == 0]
print(evens)

# Problem 2: Multiplication table
n = 5
table = [n*i for i in range(1,11)]
print(table)