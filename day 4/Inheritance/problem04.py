#. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
#operators ‘+’ and ‘*’ which adds and multiplies them.
from inheritance import Person
from Getter import Person

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imaginary_part)

    def display(self):
        print(f"Complex Number: {self.real} + {self.imaginary}i")
complex1 = Complex(2, 3)
complex2 = Complex(4, 5)
complex_sum = complex1 + complex2
complex_product = complex1 * complex2
complex_sum.display()      # Output: Complex Number: 6 + 8i
complex_product.display()  # Output: Complex Number: -7 + 22i
