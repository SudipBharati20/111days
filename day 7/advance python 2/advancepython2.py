#advance python 2
#lambda function
#lambda function is a anonymous function which is defined without a name
#it can take any number of arguments but can only have one expression
#syntax: lambda arguments: expression
#example
#normal function
def add(x, y):
    return x + y
print(add(2, 3))  # Output: 5
#lambda function
add_lambda = lambda x, y: x + y
print(add_lambda(2, 3))  # Output: 5
#lambda function can be used in higher order functions like map, filter, reduce
#map function applies a given function to all items in an iterable and returns a list of the results
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
#filter function constructs an iterator from elements of an iterable for which a function returns true
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
#reduce function applies a rolling computation to sequential pairs of values in a list
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120