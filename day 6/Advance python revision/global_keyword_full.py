"""
GLOBAL KEYWORD
"""

x = 10

def change():
    global x
    x = 50

change()
print(x)

# ------------------ PROBLEM ------------------

# Modify global variable inside function
count = 0

def increment():
    global count
    count += 1

increment()
print(count)