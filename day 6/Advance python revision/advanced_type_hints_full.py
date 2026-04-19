"""
ADVANCED TYPE HINTS
"""

from typing import List, Dict, Tuple, Union

# Example
numbers: List[int] = [1, 2, 3]
student: Tuple[str, int] = ("Ram", 20)
marks: Dict[str, int] = {"Math": 90}
value: Union[int, str] = "Hello"

# ------------------ PROBLEMS ------------------

# Problem 1: List of strings
names: List[str] = ["A", "B", "C"]
print(names)

# Problem 2: Dictionary of subjects and marks
subjects: Dict[str, int] = {"Science": 80, "English": 85}
print(subjects)

# Problem 3: Union int and float
num: Union[int, float] = 10
num = 5.5
print(num)