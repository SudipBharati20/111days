#diff between return and print
#return is used to return a value from a function, while print is used to display output to the console.
#print is used for debugging and displaying information, while return is used to pass values back to the caller of the function.

def function1():
    print("This is a print statement.")
    return "This is a return statement."

result = function1()
print(result)  # This will print the return value of the function, which is "This is a return statement."
