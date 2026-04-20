"""
REDUCE FUNCTION
"""

from functools import reduce

numbers = [1, 2, 3, 4]

sum_all = reduce(lambda x, y: x + y, numbers)

print(sum_all)