#global keyword
x = 10
def modify_global():
    global x  # Declare that we want to use the global variable x
    x += 5     # Modify the global variable
modify_global()
print(x)  # Output: 15

# Another example with a function that uses the global variable
def reset_global():
    global x  # Declare that we want to use the global variable x
    x = 0      # Reset the global variable to 0
reset_global()
print(x)  # Output: 0