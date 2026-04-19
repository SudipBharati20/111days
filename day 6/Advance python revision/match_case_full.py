"""
MATCH CASE
"""

def check_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown"

print(check_status(200))

# ------------------ PROBLEMS ------------------

# Problem 1: Grade system
def grade(g):
    match g:
        case 'A':
            return "Excellent"
        case 'B':
            return "Good"
        case _:
            return "Average"

print(grade('A'))

# Problem 2: Even/Odd using match
def even_odd(n):
    match n % 2:
        case 0:
            return "Even"
        case _:
            return "Odd"

print(even_odd(7))