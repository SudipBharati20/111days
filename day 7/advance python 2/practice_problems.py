"""
PRACTICE PROBLEMS
"""

# 1. Multiply list by 2
nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))

# 2. Filter numbers > 5
nums = [3, 7, 2, 9]
print(list(filter(lambda x: x > 5, nums)))

# 3. Find product using reduce
from functools import reduce
nums = [1, 2, 3, 4]
print(reduce(lambda x, y: x * y, nums))