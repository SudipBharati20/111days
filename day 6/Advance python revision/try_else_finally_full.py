"""
TRY ELSE FINALLY
"""

try:
    x = int(input("Enter number: "))
except:
    print("Invalid")
else:
    print("Valid:", x)
finally:
    print("Done")

# ------------------ PROBLEMS ------------------

# Problem: Division with full handling
try:
    a = int(input())
    b = int(input())
except:
    print("Input error")
else:
    print(a / b)
finally:
    print("Always runs")