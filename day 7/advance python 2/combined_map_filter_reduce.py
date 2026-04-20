"""
COMBINED EXAMPLE
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: filter even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))

# Step 2: square them
squared = list(map(lambda x: x * x, even))

# Step 3: sum them
result = reduce(lambda x, y: x + y, squared)

print(result)