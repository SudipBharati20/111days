#3. How do you prevent a python print() function to print a new line at the end. 
#You can prevent the print() function from printing a new line at the end by using the end parameter. By default, the end parameter is set to '\n', which adds a new line after the printed output. To prevent this, you can set end to an empty string ''. For example:
print("Hello, ", end="")
print("world!")  # This will print "Hello, world!" on the same line without a new line in between.