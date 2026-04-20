"""
MINI PROJECT: STUDENT MARK ANALYZER
"""

from functools import reduce

marks = [45, 67, 89, 32, 76, 50]

# Passing students
passed = list(filter(lambda x: x >= 50, marks))

# Increase marks by 5 grace
updated = list(map(lambda x: x + 5, passed))

# Total marks
total = reduce(lambda x, y: x + y, updated)

print("Passed:", passed)
print("Updated:", updated)
print("Total:", total)