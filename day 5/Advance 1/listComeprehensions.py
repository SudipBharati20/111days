#LIST COMPREHENSIONS 
#List comprehensions provide a concise way to create lists.
#The basic syntax is:
#[expression for item in iterable if condition]
#Example 1: Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Example 2: Create a list of even numbers from 0 to 19
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18

#Example 3: Create a list of uppercase letters from a string
input_string = "hello world"
uppercase_letters = [char.upper() for char in input_string if char.isalpha()]
print(uppercase_letters)  # Output: ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']