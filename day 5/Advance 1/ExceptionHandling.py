#exception Handling
try:    a = 10
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This block will always execute")

