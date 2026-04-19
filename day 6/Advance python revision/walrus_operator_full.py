"""
WALRUS OPERATOR (:=)

Definition:
The walrus operator allows assigning a value to a variable inside an expression.

Why use it?
- Reduces repeated computation
- Makes code shorter and cleaner
"""

# Example 1: Basic usage
if (length := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long: {length}")

# Example 2: Loop input
while (user := input("Enter 'q' to quit: ")) != 'q':
    print("You entered:", user)

# ------------------ PROBLEMS ------------------

# Problem 1:
# Take input until user enters 0, print sum

total = 0
while (num := int(input("Enter number (0 to stop): "))) != 0:
    total += num
print("Sum:", total)

# Problem 2:
# Use walrus operator in list comprehension

numbers = [1, 5, 10, 15]
result = [n for x in numbers if (n := x * 2) > 10]
print("Filtered:", result)