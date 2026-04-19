"""
ENUMERATE
"""

lst = ["a", "b", "c"]

for i, val in enumerate(lst):
    print(i, val)

# ------------------ PROBLEMS ------------------

# Problem: Print 3rd, 5th, 7th elements
nums = [10,20,30,40,50,60,70]

for i, val in enumerate(nums):
    if i in [2,4,6]:
        print(val)