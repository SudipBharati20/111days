"""
TYPE HINTS

Definition:
Type hints indicate expected data types of variables and functions.
"""

# Example
age: int = 22

def greet(name: str) -> str:
    return f"Hello {name}"

print(greet("Sudip"))

# ------------------ PROBLEMS ------------------

# Problem 1: Function that adds two floats
def add(a: float, b: float) -> float:
    return a + b

print(add(2.5, 3.5))

# Problem 2: Function that returns length of list
def get_length(lst: list) -> int:
    return len(lst)

print(get_length([1, 2, 3]))