"""
RAISE EXCEPTION
"""

def check_age(age):
    if age < 18:
        raise Exception("Not allowed")
    return "Allowed"

try:
    print(check_age(16))
except Exception as e:
    print(e)

# ------------------ PROBLEMS ------------------

# Problem: Raise error if number negative
def check_positive(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    return n

try:
    print(check_positive(-5))
except ValueError as e:
    print(e)