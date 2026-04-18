#types of definitions
#1. Function Definition
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!

#2. Class Definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
person = Person("Bob", 25)
print(person.introduce())  # Output: My name is Bob and I am 25 years old.

#3. Variable Definition
x = 10
y = 20
print(x + y)  # Output: 30