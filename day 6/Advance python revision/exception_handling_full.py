"""
EXCEPTION HANDLING
"""

try:
    x = int(input("Enter number: "))
    print(10 / x)
except Exception as e:
    print("Error:", e)

# ------------------ PROBLEMS ------------------

# Problem 1: Handle division
try:
    a = int(input("A: "))
    b = int(input("B: "))
    print(a / b)
except ZeroDivisionError:
    print("Infinite")

# Problem 2: Handle invalid input
try:
    num = int(input("Enter integer: "))
except ValueError:
    print("Invalid input")