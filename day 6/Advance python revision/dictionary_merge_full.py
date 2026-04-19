"""
DICTIONARY MERGE
"""

d1 = {"a": 1}
d2 = {"b": 2}

merged = d1 | d2
print(merged)

# ------------------ PROBLEMS ------------------

# Problem 1: Merge student marks
s1 = {"Math": 80}
s2 = {"Science": 90}

print(s1 | s2)

# Problem 2: Update dictionary
s1 |= s2
print(s1)