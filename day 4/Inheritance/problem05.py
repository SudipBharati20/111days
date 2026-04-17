#5. Write a class vector representing a vector of n dimensions. Overload the + and * 
#operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def display(self):
        print(f"Vector: {self.components}")
vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])
vector_sum = vector1 + vector2
dot_product = vector1 * vector2
vector_sum.display()      # Output: Vector: [5, 7, 9]
print(f"Dot Product: {dot_product}")  # Output: Dot Product: 32
